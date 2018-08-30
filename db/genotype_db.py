
# ORM definitions for Genotype
from app import db
from db.userdb import User
from db.styled_table import *
from flask_table import Table, Col, LinkCol, create_table
from db.view_table import ViewCol

class Genotype(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sequence_id = db.Column(db.String(255))
    sequences = db.Column(db.Integer)
    closest_reference = db.Column(db.String(255))
    closest_host = db.Column(db.String(255))
    nt_diff = db.Column(db.Integer)
    nt_substitutions = db.Column(db.String(255))
    aa_diff = db.Column(db.Integer)
    aa_substitutions = db.Column(db.String(255))
    unmutated_frequency = db.Column(db.Numeric)
    unmutated_sequences = db.Column(db.Integer)
    unmutated_umis = db.Column(db.Integer)
    allelic_percentage = db.Column(db.Numeric)
    unique_ds = db.Column(db.Integer)
    unique_js = db.Column(db.Integer)
    unique_cdr3s = db.Column(db.Integer)
    haplotyping_locus = db.Column(db.String(255))
    haplotyping_ratio = db.Column(db.String(255))
    nt_sequence = db.Column(db.String(1000))
    description_id = db.Column(db.Integer, db.ForeignKey('genotype_description.id'))
    genotype_description = db.relationship('GenotypeDescription', backref = 'genotypes')


def save_Genotype(db, object, form, new=False):   
    object.sequence_id = form.sequence_id.data
    object.sequences = form.sequences.data
    object.closest_reference = form.closest_reference.data
    object.closest_host = form.closest_host.data
    object.nt_diff = form.nt_diff.data
    object.nt_substitutions = form.nt_substitutions.data
    object.aa_diff = form.aa_diff.data
    object.aa_substitutions = form.aa_substitutions.data
    object.unmutated_frequency = form.unmutated_frequency.data
    object.unmutated_sequences = form.unmutated_sequences.data
    object.unmutated_umis = form.unmutated_umis.data
    object.allelic_percentage = form.allelic_percentage.data
    object.unique_ds = form.unique_ds.data
    object.unique_js = form.unique_js.data
    object.unique_cdr3s = form.unique_cdr3s.data
    object.haplotyping_locus = form.haplotyping_locus.data
    object.haplotyping_ratio = form.haplotyping_ratio.data
    object.nt_sequence = form.nt_sequence.data

    if new:
        db.session.add(object)
        
    db.session.commit()   



def populate_Genotype(db, object, form):   
    form.sequence_id.data = object.sequence_id
    form.sequences.data = object.sequences
    form.closest_reference.data = object.closest_reference
    form.closest_host.data = object.closest_host
    form.nt_diff.data = object.nt_diff
    form.nt_substitutions.data = object.nt_substitutions
    form.aa_diff.data = object.aa_diff
    form.aa_substitutions.data = object.aa_substitutions
    form.unmutated_frequency.data = object.unmutated_frequency
    form.unmutated_sequences.data = object.unmutated_sequences
    form.unmutated_umis.data = object.unmutated_umis
    form.allelic_percentage.data = object.allelic_percentage
    form.unique_ds.data = object.unique_ds
    form.unique_js.data = object.unique_js
    form.unique_cdr3s.data = object.unique_cdr3s
    form.haplotyping_locus.data = object.haplotyping_locus
    form.haplotyping_ratio.data = object.haplotyping_ratio
    form.nt_sequence.data = object.nt_sequence



class Genotype_table(StyledTable):
    id = Col("id", show=False)
    sequence_id = StyledCol("Allele name", tooltip="Identifier of the allele (either IMGT, or the name assigned by the submitter to an inferred gene)")
    sequences = StyledCol("Sequences", tooltip="Overall number of sequences assigned to this allele")
    closest_reference = StyledCol("Closest Reference", tooltip="For inferred alleles, the closest reference gene and allele, as inferred by the tool")
    closest_host = StyledCol("Closest in Host", tooltip="For inferred alleles, the closest reference gene and allele that is in the subject's inferred genotype, as inferred by the tool")
    nt_diff = StyledCol("NT Diffs", tooltip="For inferred alleles, the number of nucleotides that differ between this sequence and the closest reference gene and allele")
    nt_substitutions = StyledCol("NT Substs", tooltip="Comma-separated list of nucleotide substitutions (e.g. G112A) between this sequence and the closest reference gene and allele")
    aa_diff = StyledCol("AA Diffs", tooltip="For inferred alleles, the number of amino acids that differ between this sequence and the closest reference gene and allele")
    aa_substitutions = StyledCol("AA Substs", tooltip="List of amino acid substitutions (e.g. A96N) between this sequence and the closest reference gene and allele. Please use IMGT numbering for V-genes, and number from start of coding sequence for D- or J- genes.")
    unmutated_frequency = StyledCol("Unmutated Freq", tooltip="The number of sequences exactly matching the sequence of this allele divided by the number of sequences exactly matching any allele of any gene, *100")
    unmutated_sequences = StyledCol("Unmutated Seqs", tooltip="he number of sequences exactly matching this unmutated sequence")
    unmutated_umis = StyledCol("Unmutated UMIs", tooltip="The number of molecules (identified by Unique Molecular Identifiers) exactly matching this unmutated sequence (if UMIs were used)")
    allelic_percentage = StyledCol("Allelic %", tooltip="The number of sequences exactly matching the sequence of this allele divided by the number of sequences exactly matching any allele of this specific gene, *100")
    unique_ds = StyledCol("Unique Ds", tooltip="Number of D allele calls (i.e., unique allelic sequences) found associated with an inferred V sequence")
    unique_js = StyledCol("Unique Js", tooltip="Number of J allele calls (i.e., unique allelic sequences) found associated with an inferred V sequence")
    unique_cdr3s = StyledCol("Unique CDR3s", tooltip="Number of unique CDR3s found associated with an inferred V sequence")
    haplotyping_locus = StyledCol("Haplotyping Locus", tooltip="Locus (or loci) from which haplotyping was inferred (e.g. IGHJ6)")
    haplotyping_ratio = StyledCol("Haplotyping Ratio", tooltip="Ratio (expressed as two percentages) with which the two inferred haplotypes were found (e.g. 60:40)")


def make_Genotype_table(results, private = False, classes=()):
    t=create_table(base=Genotype_table)
    ret = t(results, classes=classes)
    return ret

class Genotype_view(Table):
    item = ViewCol("", column_html_attrs={"class": "col-sm-3 text-right font-weight-bold view-table-row"})
    value = Col("")


def make_Genotype_view(sub, private = False):
    ret = Genotype_view([])
    ret.items.append({"item": "Allele name", "value": sub.sequence_id, "tooltip": "Identifier of the allele (either IMGT, or the name assigned by the submitter to an inferred gene)"})
    ret.items.append({"item": "Sequences", "value": sub.sequences, "tooltip": "Overall number of sequences assigned to this allele"})
    ret.items.append({"item": "Closest Reference", "value": sub.closest_reference, "tooltip": "For inferred alleles, the closest reference gene and allele, as inferred by the tool"})
    ret.items.append({"item": "Closest in Host", "value": sub.closest_host, "tooltip": "For inferred alleles, the closest reference gene and allele that is in the subject's inferred genotype, as inferred by the tool"})
    ret.items.append({"item": "NT Diffs", "value": sub.nt_diff, "tooltip": "For inferred alleles, the number of nucleotides that differ between this sequence and the closest reference gene and allele"})
    ret.items.append({"item": "NT Substs", "value": sub.nt_substitutions, "tooltip": "Comma-separated list of nucleotide substitutions (e.g. G112A) between this sequence and the closest reference gene and allele"})
    ret.items.append({"item": "AA Diffs", "value": sub.aa_diff, "tooltip": "For inferred alleles, the number of amino acids that differ between this sequence and the closest reference gene and allele"})
    ret.items.append({"item": "AA Substs", "value": sub.aa_substitutions, "tooltip": "List of amino acid substitutions (e.g. A96N) between this sequence and the closest reference gene and allele. Please use IMGT numbering for V-genes, and number from start of coding sequence for D- or J- genes."})
    ret.items.append({"item": "Unmutated Freq", "value": sub.unmutated_frequency, "tooltip": "The number of sequences exactly matching the sequence of this allele divided by the number of sequences exactly matching any allele of any gene, *100"})
    ret.items.append({"item": "Unmutated Seqs", "value": sub.unmutated_sequences, "tooltip": "he number of sequences exactly matching this unmutated sequence"})
    ret.items.append({"item": "Unmutated UMIs", "value": sub.unmutated_umis, "tooltip": "The number of molecules (identified by Unique Molecular Identifiers) exactly matching this unmutated sequence (if UMIs were used)"})
    ret.items.append({"item": "Allelic %", "value": sub.allelic_percentage, "tooltip": "The number of sequences exactly matching the sequence of this allele divided by the number of sequences exactly matching any allele of this specific gene, *100"})
    ret.items.append({"item": "Unique Ds", "value": sub.unique_ds, "tooltip": "Number of D allele calls (i.e., unique allelic sequences) found associated with an inferred V sequence"})
    ret.items.append({"item": "Unique Js", "value": sub.unique_js, "tooltip": "Number of J allele calls (i.e., unique allelic sequences) found associated with an inferred V sequence"})
    ret.items.append({"item": "Unique CDR3s", "value": sub.unique_cdr3s, "tooltip": "Number of unique CDR3s found associated with an inferred V sequence"})
    ret.items.append({"item": "Haplotyping Locus", "value": sub.haplotyping_locus, "tooltip": "Locus (or loci) from which haplotyping was inferred (e.g. IGHJ6)"})
    ret.items.append({"item": "Haplotyping Ratio", "value": sub.haplotyping_ratio, "tooltip": "Ratio (expressed as two percentages) with which the two inferred haplotypes were found (e.g. 60:40)"})
    ret.items.append({"item": "NT Sequence", "value": sub.nt_sequence, "tooltip": "The consensus sequence provided by the inference tool"})
    return ret

