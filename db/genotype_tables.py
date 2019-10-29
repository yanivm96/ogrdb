
# ORM definitions for Genotype
# This file is automatically generated from the schema by schema/build_from_schema.py

from app import db
from db.styled_table import *
from flask_table import Table, Col, LinkCol, create_table
from db.view_table import ViewCol

class Genotype_novel_table(StyledTable):
    id = Col("id", show=False)
    sequence_id = StyledCol("Allele name", tooltip="Identifier of the allele (either IMGT, or the name assigned by the submitter to an inferred gene)")
    sequences = StyledCol("Sequences", tooltip="Overall number of sequences assigned to this allele")
    closest_reference = StyledCol("Closest Reference", tooltip="For inferred alleles, the closest reference gene and allele, as inferred by the tool")
    closest_host = StyledCol("Closest in Host", tooltip="For inferred alleles, the closest reference gene and allele that is in the subject's inferred genotype")
    nt_diff = StyledCol("NT Diffs (reference)", tooltip="For inferred alleles, the number of nucleotides that differ between this sequence and the closest reference gene and allele")
    nt_diff_host = StyledCol("NT Diffs (host)", tooltip="For inferred alleles, the number of nucleotides that differ between this sequence and the closest reference gene and allele that is in the subject's inferred genotype")
    nt_substitutions = StyledCol("NT Substs (reference)", tooltip="For inferred alleles, Comma-separated list of nucleotide substitutions (e.g. G112A) between this sequence and the closest reference gene and allele. Please use IMGT numbering for V-genes, and number from start of coding sequence for D- or J- genes.")
    aa_diff = StyledCol("AA Diffs (reference)", tooltip="For inferred alleles, the number of amino acids that differ between this sequence and the closest reference gene and allele")
    aa_substitutions = StyledCol("AA Substs (reference)", tooltip="For inferred alleles, the list of amino acid substitutions (e.g. A96N) between this sequence and the closest reference gene and allele. Please use IMGT numbering for V-genes, and number from start of coding sequence for D- or J- genes.")


def make_Genotype_novel_table(results, private = False, classes=()):
    t=create_table(base=Genotype_novel_table)
    return t(results, classes=classes)


class Genotype_full_table(StyledTable):
    id = Col("id", show=False)
    sequence_id = StyledCol("Allele name", tooltip="Identifier of the allele (either IMGT, or the name assigned by the submitter to an inferred gene)")
    sequences = StyledCol("Sequences", tooltip="Overall number of sequences assigned to this allele")
    unmutated_sequences = StyledCol("Unmutated Seqs", tooltip="The number of sequences exactly matching this unmutated sequence")
    assigned_unmutated_frequency = StyledCol("Unmutated % within allele", tooltip="The number of sequences exactly matching this allele divided by the number of sequences assigned to this allele, *100")
    unmutated_umis = StyledCol("Unmutated UMIs", tooltip="The number of molecules (identified by Unique Molecular Identifiers) exactly matching this unmutated sequence (if UMIs were used)")
    allelic_percentage = StyledCol("Allelic %", tooltip="The number of sequences exactly matching the sequence of this allele divided by the number of sequences exactly matching any allele of this specific gene, *100")
    unmutated_frequency = StyledCol("Total unmutated population (%)", tooltip="The number of sequences exactly matching the sequence of this allele divided by the number of sequences exactly matching any allele of any gene, *100")
    unique_vs = StyledCol("Unique Vs", tooltip="The number of V allele calls (i.e., unique allelic sequences) associated with this allele")
    unique_ds = StyledCol("Unique Ds", tooltip="The number of D allele calls (i.e., unique allelic sequences) associated with this allele")
    unique_js = StyledCol("Unique Js", tooltip="The number of J allele calls (i.e., unique allelic sequences) associated with this allele")
    unique_cdr3s = StyledCol("Unique CDR3s", tooltip="The number of unique CDR3s associated with this allele")
    unique_vs_unmutated = StyledCol("Unique Vs with unmutated", tooltip="The number of V allele calls (i.e., unique allelic sequences) associated with unmutated sequences of this allele")
    unique_ds_unmutated = StyledCol("Unique Ds with unmutated", tooltip="The number of D allele calls (i.e., unique allelic sequences) associated with unmutated sequences of this allele")
    unique_js_unmutated = StyledCol("Unique Js with unmutated", tooltip="The number of J allele calls (i.e., unique allelic sequences) associated with unmutated sequences of this allele")
    unique_cdr3s_unmutated = StyledCol("Unique CDR3s with unmutated", tooltip="The number of unique CDR3s associated with unmutated sequences of this allele")
    haplotyping_gene = StyledCol("Haplotyping Gene", tooltip="The gene (or genes) from which haplotyping was inferred (e.g. IGHJ6)")
    haplotyping_ratio = StyledCol("Haplotyping Ratio", tooltip="The ratio (expressed as two percentages) with which the two inferred haplotypes were found (e.g. 60:40)")


def make_Genotype_full_table(results, segment, private = False, classes=()):
    t=create_table(base=Genotype_full_table)
    if segment not in ["D", "JH", "JL"]:
        t._cols["unique_vs"].show = False
    if segment not in ["VH", "JH"]:
        t._cols["unique_ds"].show = False
    if segment not in ["VH", "D", "VL"]:
        t._cols["unique_js"].show = False
    if segment not in ["D", "JH", "JL"]:
        t._cols["unique_vs_unmutated"].show = False
    if segment not in ["VH", "JH"]:
        t._cols["unique_ds_unmutated"].show = False
    if segment not in ["VH", "D", "VL"]:
        t._cols["unique_js_unmutated"].show = False
    return t(results, classes=classes)


reqd_gen_fields = {
    "D": ["sequence_id", "sequences", "closest_reference", "closest_host", "nt_diff", "nt_diff_host", "nt_substitutions", "aa_diff", "aa_substitutions", "unmutated_sequences", "assigned_unmutated_frequency", "allelic_percentage", "unmutated_frequency", "unique_vs", "unique_js", "unique_cdr3s", "unique_vs_unmutated", "unique_js_unmutated", "nt_sequence"],
    "JH": ["sequence_id", "sequences", "closest_reference", "closest_host", "nt_diff", "nt_diff_host", "nt_substitutions", "aa_diff", "aa_substitutions", "unmutated_sequences", "assigned_unmutated_frequency", "allelic_percentage", "unmutated_frequency", "unique_vs", "unique_ds", "unique_cdr3s", "unique_vs_unmutated", "unique_ds_unmutated", "nt_sequence"],
    "JL": ["sequence_id", "sequences", "closest_reference", "closest_host", "nt_diff", "nt_diff_host", "nt_substitutions", "aa_diff", "aa_substitutions", "unmutated_sequences", "assigned_unmutated_frequency", "allelic_percentage", "unmutated_frequency", "unique_vs", "unique_cdr3s", "unique_vs_unmutated", "nt_sequence"],
    "VH": ["sequence_id", "sequences", "closest_reference", "closest_host", "nt_diff", "nt_diff_host", "nt_substitutions", "aa_diff", "aa_substitutions", "unmutated_sequences", "assigned_unmutated_frequency", "allelic_percentage", "unmutated_frequency", "unique_ds", "unique_js", "unique_cdr3s", "unique_ds_unmutated", "unique_js_unmutated", "nt_sequence"],
    "VL": ["sequence_id", "sequences", "closest_reference", "closest_host", "nt_diff", "nt_diff_host", "nt_substitutions", "aa_diff", "aa_substitutions", "unmutated_sequences", "assigned_unmutated_frequency", "allelic_percentage", "unmutated_frequency", "unique_js", "unique_cdr3s", "unique_js_unmutated", "nt_sequence"],
}
