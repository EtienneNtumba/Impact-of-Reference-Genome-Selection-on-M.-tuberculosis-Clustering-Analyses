#!/usr/bin/env nextflow

// Define parameters
params.reads = '/path/to/fastq/files/*.fastq'
params.reference = '/path/to/reference/genome.fasta'
params.outdir = './results'

// Define channels
channel.fromFilePairs(params.reads).set { sample_id, reads }
channel.fromPath(params.reference).set { reference }

// Process: Basecalling is skipped here as we assume FASTQ input
process QualityControl {
    input:
    set sample_id, file(reads) from reads

    output:
    file("${sample_id}_qc.html") into qc_reports

    script:
    """
    NanoPlot --fastq $reads --outdir ${sample_id}_qc --plots hex dot
    """
}

process ReadFiltering {
    input:
    set sample_id, file(reads) from reads

    output:
    file("${sample_id}_filtered.fastq") into filtered_reads

    script:
    """
    filtlong --min_length 1000 --keep_percent 90 $reads > ${sample_id}_filtered.fastq
    """
}

process AlignReads {
    input:
    set sample_id, file(filtered_reads) from filtered_reads
    file reference from reference

    output:
    file("${sample_id}.bam") into bam_files

    script:
    """
    minimap2 -ax map-ont $reference ${sample_id}_filtered.fastq | samtools sort -o ${sample_id}.bam
    samtools index ${sample_id}.bam
    """
}

process VariantCalling {
    input:
    set sample_id, file(bam) from bam_files
    file reference from reference

    output:
    file("${sample_id}_variants.vcf") into variant_files

    script:
    """
    nanopolish variants --bam $bam --genome $reference --outfile ${sample_id}_variants.vcf
    """
}

process VariantAnnotation {
    input:
    set sample_id, file(vcf) from variant_files
    file reference from reference

    output:
    file("${sample_id}_annotated.vcf") into annotated_vcfs

    script:
    """
    snpEff -c snpEff.config TB $vcf > ${sample_id}_annotated.vcf
    """
}

// Workflow execution order
workflow {
    reads | QualityControl | ReadFiltering | AlignReads | VariantCalling | VariantAnnotation
}
