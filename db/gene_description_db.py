
# ORM definitions for GeneDescription
# This file is automatically generated from the schema by schema/build_from_schema.py

from app import db
from db.userdb import User
from db.styled_table import *
from flask_table import Table, Col, LinkCol, create_table
from db.view_table import ViewCol
from sqlalchemy.orm import backref


inferred_sequences_gene_descriptions = db.Table('inferred_sequences_gene_descriptions',
    db.Column('inferred_sequences_id', db.Integer(), db.ForeignKey('inferred_sequence.id')),
    db.Column('gene_descriptions_id', db.Integer(), db.ForeignKey('gene_description.id')))



supporting_observations_supporting_gene_descriptions = db.Table('supporting_observations_supporting_gene_descriptions',
    db.Column('supporting_observations_id', db.Integer(), db.ForeignKey('genotype.id')),
    db.Column('supporting_gene_descriptions_id', db.Integer(), db.ForeignKey('gene_description.id')))



duplicate_sequences_published_duplicates = db.Table('duplicate_sequences_published_duplicates',
    db.Column('duplicate_sequences_id', db.Integer(), db.ForeignKey('genotype.id')),
    db.Column('published_duplicates_id', db.Integer(), db.ForeignKey('gene_description.id')))


from db._gene_description_db import *

class GeneDescription(db.Model, GeneDescriptionMixin):
    id = db.Column(db.Integer, primary_key=True)
    description_id = db.Column(db.String(1000))
    maintainer = db.Column(db.String(1000))
    lab_address = db.Column(db.String(1000))
    release_version = db.Column(db.Integer)
    release_date = db.Column(db.DateTime)
    release_description = db.Column(db.Text())

    imgt_name = db.Column(db.String(1000))
    sequence_name = db.Column(db.String(1000))
    alt_names = db.Column(db.String(1000))
    chromosome = db.Column(db.Integer)
    locus = db.Column(db.String(255))
    sequence_type = db.Column(db.String(255))
    functional = db.Column(db.Boolean)
    inference_type = db.Column(db.String(255))
    affirmation_level = db.Column(db.String(255))
    species = db.Column(db.String(1000))
    species_subgroup = db.Column(db.String(1000))
    species_subgroup_type = db.Column(db.String(255))
    status = db.Column(db.String(255))
    gene_subgroup = db.Column(db.String(1000))
    subgroup_designation = db.Column(db.String(1000))
    allele_designation = db.Column(db.String(1000))
    sequence = db.Column(db.Text())
    coding_seq_imgt = db.Column(db.Text())
    coding_sequence_identifier = db.Column(db.String(1000))
    gene_start = db.Column(db.Integer)
    gene_end = db.Column(db.Integer)
    utr_5_prime_start = db.Column(db.Integer)
    utr_5_prime_end = db.Column(db.Integer)
    leader_1_start = db.Column(db.Integer)
    leader_1_end = db.Column(db.Integer)
    leader_2_start = db.Column(db.Integer)
    leader_2_end = db.Column(db.Integer)
    v_rs_start = db.Column(db.Integer)
    v_rs_end = db.Column(db.Integer)
    d_rs_3_prime_start = db.Column(db.Integer)
    d_rs_3_prime_end = db.Column(db.Integer)
    d_rs_5_prime_start = db.Column(db.Integer)
    d_rs_5_prime_end = db.Column(db.Integer)
    j_rs_start = db.Column(db.Integer)
    j_rs_end = db.Column(db.Integer)
    j_codon_frame = db.Column(db.String(255))
    j_cdr3_end = db.Column(db.Integer)
    paralogs = db.Column(db.String(1000))
    notes = db.Column(db.Text())

    inferred_sequences = db.relationship('InferredSequence', secondary=inferred_sequences_gene_descriptions, backref=db.backref('gene_descriptions', lazy='dynamic'))

    supporting_observations = db.relationship('Genotype', secondary=supporting_observations_supporting_gene_descriptions, backref=db.backref('supporting_gene_descriptions', lazy='dynamic'))

    duplicate_sequences = db.relationship('Genotype', secondary=duplicate_sequences_published_duplicates, backref=db.backref('published_duplicates', lazy='dynamic'))
    inferred_extension = db.Column(db.Boolean)
    ext_3prime = db.Column(db.Text())
    start_3prime_ext = db.Column(db.Integer)
    end_3prime_ext = db.Column(db.Integer)
    ext_5prime = db.Column(db.Text())
    start_5prime_ext = db.Column(db.Integer)
    end_5prime_ext = db.Column(db.Integer)
    curational_tags = db.Column(db.String(255))


def save_GeneDescription(db, object, form, new=False):
    object.maintainer = form.maintainer.data
    object.lab_address = form.lab_address.data
    object.imgt_name = form.imgt_name.data
    object.sequence_name = form.sequence_name.data
    object.alt_names = form.alt_names.data
    object.chromosome = form.chromosome.data
    object.locus = form.locus.data
    object.sequence_type = form.sequence_type.data
    object.functional = form.functional.data
    object.inference_type = form.inference_type.data
    object.affirmation_level = form.affirmation_level.data
    object.species_subgroup = form.species_subgroup.data
    object.species_subgroup_type = form.species_subgroup_type.data
    object.gene_subgroup = form.gene_subgroup.data
    object.subgroup_designation = form.subgroup_designation.data
    object.allele_designation = form.allele_designation.data
    object.sequence = form.sequence.data
    object.coding_seq_imgt = form.coding_seq_imgt.data
    object.gene_start = form.gene_start.data
    object.gene_end = form.gene_end.data
    object.utr_5_prime_start = form.utr_5_prime_start.data
    object.utr_5_prime_end = form.utr_5_prime_end.data
    object.leader_1_start = form.leader_1_start.data
    object.leader_1_end = form.leader_1_end.data
    object.leader_2_start = form.leader_2_start.data
    object.leader_2_end = form.leader_2_end.data
    object.v_rs_start = form.v_rs_start.data
    object.v_rs_end = form.v_rs_end.data
    object.d_rs_3_prime_start = form.d_rs_3_prime_start.data
    object.d_rs_3_prime_end = form.d_rs_3_prime_end.data
    object.d_rs_5_prime_start = form.d_rs_5_prime_start.data
    object.d_rs_5_prime_end = form.d_rs_5_prime_end.data
    object.j_rs_start = form.j_rs_start.data
    object.j_rs_end = form.j_rs_end.data
    object.j_codon_frame = form.j_codon_frame.data
    object.j_cdr3_end = form.j_cdr3_end.data
    object.paralogs = form.paralogs.data
    object.inferred_extension = form.inferred_extension.data
    object.ext_3prime = form.ext_3prime.data
    object.start_3prime_ext = form.start_3prime_ext.data
    object.end_3prime_ext = form.end_3prime_ext.data
    object.ext_5prime = form.ext_5prime.data
    object.start_5prime_ext = form.start_5prime_ext.data
    object.end_5prime_ext = form.end_5prime_ext.data
    object.curational_tags = form.curational_tags.data

    if new:
        db.session.add(object)

    db.session.commit()



def populate_GeneDescription(db, object, form):
    form.maintainer.data = object.maintainer
    form.lab_address.data = object.lab_address
    form.imgt_name.data = object.imgt_name
    form.sequence_name.data = object.sequence_name
    form.alt_names.data = object.alt_names
    form.chromosome.data = object.chromosome
    form.locus.data = object.locus
    form.sequence_type.data = object.sequence_type
    form.functional.data = object.functional
    form.inference_type.data = object.inference_type
    form.affirmation_level.data = object.affirmation_level
    form.species_subgroup.data = object.species_subgroup
    form.species_subgroup_type.data = object.species_subgroup_type
    form.gene_subgroup.data = object.gene_subgroup
    form.subgroup_designation.data = object.subgroup_designation
    form.allele_designation.data = object.allele_designation
    form.sequence.data = object.sequence
    form.coding_seq_imgt.data = object.coding_seq_imgt
    form.gene_start.data = object.gene_start
    form.gene_end.data = object.gene_end
    form.utr_5_prime_start.data = object.utr_5_prime_start
    form.utr_5_prime_end.data = object.utr_5_prime_end
    form.leader_1_start.data = object.leader_1_start
    form.leader_1_end.data = object.leader_1_end
    form.leader_2_start.data = object.leader_2_start
    form.leader_2_end.data = object.leader_2_end
    form.v_rs_start.data = object.v_rs_start
    form.v_rs_end.data = object.v_rs_end
    form.d_rs_3_prime_start.data = object.d_rs_3_prime_start
    form.d_rs_3_prime_end.data = object.d_rs_3_prime_end
    form.d_rs_5_prime_start.data = object.d_rs_5_prime_start
    form.d_rs_5_prime_end.data = object.d_rs_5_prime_end
    form.j_rs_start.data = object.j_rs_start
    form.j_rs_end.data = object.j_rs_end
    form.j_codon_frame.data = object.j_codon_frame
    form.j_cdr3_end.data = object.j_cdr3_end
    form.paralogs.data = object.paralogs
    form.inferred_extension.data = object.inferred_extension
    form.ext_3prime.data = object.ext_3prime
    form.start_3prime_ext.data = object.start_3prime_ext
    form.end_3prime_ext.data = object.end_3prime_ext
    form.ext_5prime.data = object.ext_5prime
    form.start_5prime_ext.data = object.start_5prime_ext
    form.end_5prime_ext.data = object.end_5prime_ext
    form.curational_tags.data = object.curational_tags




def copy_GeneDescription(c_from, c_to):
    c_to.maintainer = c_from.maintainer
    c_to.lab_address = c_from.lab_address
    c_to.release_version = c_from.release_version
    c_to.release_date = c_from.release_date
    c_to.release_description = c_from.release_description
    c_to.imgt_name = c_from.imgt_name
    c_to.sequence_name = c_from.sequence_name
    c_to.alt_names = c_from.alt_names
    c_to.chromosome = c_from.chromosome
    c_to.locus = c_from.locus
    c_to.sequence_type = c_from.sequence_type
    c_to.functional = c_from.functional
    c_to.inference_type = c_from.inference_type
    c_to.affirmation_level = c_from.affirmation_level
    c_to.species = c_from.species
    c_to.species_subgroup = c_from.species_subgroup
    c_to.species_subgroup_type = c_from.species_subgroup_type
    c_to.status = c_from.status
    c_to.gene_subgroup = c_from.gene_subgroup
    c_to.subgroup_designation = c_from.subgroup_designation
    c_to.allele_designation = c_from.allele_designation
    c_to.sequence = c_from.sequence
    c_to.coding_seq_imgt = c_from.coding_seq_imgt
    c_to.coding_sequence_identifier = c_from.coding_sequence_identifier
    c_to.gene_start = c_from.gene_start
    c_to.gene_end = c_from.gene_end
    c_to.utr_5_prime_start = c_from.utr_5_prime_start
    c_to.utr_5_prime_end = c_from.utr_5_prime_end
    c_to.leader_1_start = c_from.leader_1_start
    c_to.leader_1_end = c_from.leader_1_end
    c_to.leader_2_start = c_from.leader_2_start
    c_to.leader_2_end = c_from.leader_2_end
    c_to.v_rs_start = c_from.v_rs_start
    c_to.v_rs_end = c_from.v_rs_end
    c_to.d_rs_3_prime_start = c_from.d_rs_3_prime_start
    c_to.d_rs_3_prime_end = c_from.d_rs_3_prime_end
    c_to.d_rs_5_prime_start = c_from.d_rs_5_prime_start
    c_to.d_rs_5_prime_end = c_from.d_rs_5_prime_end
    c_to.j_rs_start = c_from.j_rs_start
    c_to.j_rs_end = c_from.j_rs_end
    c_to.j_codon_frame = c_from.j_codon_frame
    c_to.j_cdr3_end = c_from.j_cdr3_end
    c_to.paralogs = c_from.paralogs
    c_to.notes = c_from.notes
    c_to.inferred_extension = c_from.inferred_extension
    c_to.ext_3prime = c_from.ext_3prime
    c_to.start_3prime_ext = c_from.start_3prime_ext
    c_to.end_3prime_ext = c_from.end_3prime_ext
    c_to.ext_5prime = c_from.ext_5prime
    c_to.start_5prime_ext = c_from.start_5prime_ext
    c_to.end_5prime_ext = c_from.end_5prime_ext
    c_to.curational_tags = c_from.curational_tags



class GeneDescription_table(StyledTable):
    id = Col("id", show=False)
    imgt_name = StyledCol("IUIS Name", tooltip="The name of this sequence as assigned by IUIS")
    locus = StyledCol("Locus", tooltip="Gene locus")
    sequence_type = StyledCol("Sequence Type", tooltip="Sequence type (V, D, J, CH1 ... CH4, Leader)")
    affirmation_level = StyledCol("Affirmation Level", tooltip="Count of independent studies in which this allele as been affirmed by IARC (1,2,3 or more)")
    species = StyledCol("Species", tooltip="Binomial designation of subject's species")
    coding_sequence_identifier = StyledCol("Seq ID", tooltip="Unique identifier of the coding_sequence, allocated automatically")


def make_GeneDescription_table(results, private = False, classes=()):
    t = create_table(base=GeneDescription_table)
    ret = t(results, classes=classes)
    return ret

class GeneDescription_view(Table):
    item = ViewCol("", column_html_attrs={"class": "col-sm-3 text-right font-weight-bold view-table-row"})
    value = Col("")


def make_GeneDescription_view(sub, private = False):
    ret = GeneDescription_view([])
    ret.items.append({"item": "Sequence ID", "value": sub.description_id, "tooltip": "Unique identifier of this gene sequence", "field": "description_id"})
    ret.items.append({"item": "Curator", "value": sub.maintainer, "tooltip": "Maintainer of this sequence record", "field": "maintainer"})
    ret.items.append({"item": "Curator address", "value": sub.lab_address, "tooltip": "Institution and full address of corresponding author", "field": "lab_address"})
    ret.items.append({"item": "Version", "value": sub.release_version, "tooltip": "Version number of this record, updated whenever a revised version is published or released", "field": "release_version"})
    ret.items.append({"item": "Release Date", "value": sub.release_date, "tooltip": "Date of this release", "field": "release_date"})
    ret.items.append({"item": "Release Notes", "value": sub.release_description, "tooltip": "Brief descriptive notes of the reason for this release and the changes embodied", "field": "release_description"})
    ret.items.append({"item": "IUIS Name", "value": sub.imgt_name, "tooltip": "The name of this sequence as assigned by IUIS", "field": "imgt_name"})
    ret.items.append({"item": "Sequence Name", "value": sub.sequence_name, "tooltip": "The canonical name of this sequence as assigned by IARC", "field": "sequence_name"})
    ret.items.append({"item": "Alternative names", "value": sub.alt_names, "tooltip": "Alternative names for this sequence", "field": "alt_names"})
    ret.items.append({"item": "Chromosome", "value": sub.chromosome, "tooltip": "chromosome on which the gene is located", "field": "chromosome"})
    ret.items.append({"item": "Locus", "value": sub.locus, "tooltip": "Gene locus", "field": "locus"})
    ret.items.append({"item": "Sequence Type", "value": sub.sequence_type, "tooltip": "Sequence type (V, D, J, CH1 ... CH4, Leader)", "field": "sequence_type"})
    ret.items.append({"item": "Functional", "value": sub.functional, "tooltip": "Functional", "field": "functional"})
    ret.items.append({"item": "Inference Type", "value": sub.inference_type, "tooltip": "Type of inference(s) from which this gene sequence was inferred (Genomic and Rearranged, Genomic Only, Rearranged Only)", "field": "inference_type"})
    ret.items.append({"item": "Affirmation Level", "value": sub.affirmation_level, "tooltip": "Count of independent studies in which this allele as been affirmed by IARC (1,2,3 or more)", "field": "affirmation_level"})
    ret.items.append({"item": "Species", "value": sub.species, "tooltip": "Binomial designation of subject's species", "field": "species"})
    ret.items.append({"item": "Species subgroup", "value": sub.species_subgroup, "tooltip": "Race, strain or other species subgroup to which this subject belongs", "field": "species_subgroup"})
    ret.items.append({"item": "Subgroup type", "value": sub.species_subgroup_type, "tooltip": "Category of subgroup", "field": "species_subgroup_type"})
    ret.items.append({"item": "Gene Subgroup", "value": sub.gene_subgroup, "tooltip": "Gene subgroup (family), as (and if) identified for this species and gene", "field": "gene_subgroup"})
    ret.items.append({"item": "Gene Designation", "value": sub.subgroup_designation, "tooltip": "Gene designation within this subgroup, if identified", "field": "subgroup_designation"})
    ret.items.append({"item": "Allele Designation", "value": sub.allele_designation, "tooltip": "Allele designation, if identified", "field": "allele_designation"})
    ret.items.append({"item": "Full Sequence", "value": sub.sequence, "tooltip": "nt sequence of the gene. This should cover the full length that is available, including where possible 5' UTR and lead-in for V-gene sequences", "field": "sequence"})
    ret.items.append({"item": "Coding Sequence", "value": sub.coding_seq_imgt, "tooltip": "nucleotide sequence of the coding region, aligned, in the case of a V-gene, with the IMGT numbering scheme", "field": "coding_seq_imgt"})
    ret.items.append({"item": "Seq ID", "value": sub.coding_sequence_identifier, "tooltip": "Unique identifier of the coding_sequence, allocated automatically", "field": "coding_sequence_identifier"})
    ret.items.append({"item": "Gene start", "value": sub.gene_start, "tooltip": "Co-ordinate (in the sequence field) of the first nucleotide in the coding_sequence field", "field": "gene_start"})
    ret.items.append({"item": "Gene end", "value": sub.gene_end, "tooltip": "Co-ordinate (in the sequence field) of the last gene-coding nucleotide in the coding_sequence field", "field": "gene_end"})
    ret.items.append({"item": "UTR 5\' Start", "value": sub.utr_5_prime_start, "tooltip": "Start co-ordinate in the Full Sequence of 5 prime UTR (V-genes only)", "field": "utr_5_prime_start"})
    ret.items.append({"item": "UTR 5\' End", "value": sub.utr_5_prime_end, "tooltip": "End co-ordinate in the Full Sequence of 5 prime UTR (V-genes only)", "field": "utr_5_prime_end"})
    ret.items.append({"item": "L-PART1 Start", "value": sub.leader_1_start, "tooltip": "Start co-ordinate in the Full Sequence of L-PART1 (V-genes only)", "field": "leader_1_start"})
    ret.items.append({"item": "L-PART1 End", "value": sub.leader_1_end, "tooltip": "End co-ordinate in the Full Sequence of L-PART1 (V-genes only)", "field": "leader_1_end"})
    ret.items.append({"item": "L-PART2 Start", "value": sub.leader_2_start, "tooltip": "Start co-ordinate in the Full Sequence of L-PART2 (V-genes only)", "field": "leader_2_start"})
    ret.items.append({"item": "L-PART2 End", "value": sub.leader_2_end, "tooltip": "End co-ordinate in the Full Sequence of L-PART2 (V-genes only)", "field": "leader_2_end"})
    ret.items.append({"item": "v_rs_start", "value": sub.v_rs_start, "tooltip": "Start co-ordinate in the Full Sequence of V recombination site (V-genes only)", "field": "v_rs_start"})
    ret.items.append({"item": "v_rs_end", "value": sub.v_rs_end, "tooltip": "End co-ordinate in the Full Sequence of V recombination site (V-genes only)", "field": "v_rs_end"})
    ret.items.append({"item": "d_rs_3_prime_start", "value": sub.d_rs_3_prime_start, "tooltip": "Start co-ordinate in the Full Sequence of 3 prime D recombination site (D-genes only)", "field": "d_rs_3_prime_start"})
    ret.items.append({"item": "d_rs_3_prime_end", "value": sub.d_rs_3_prime_end, "tooltip": "End co-ordinate in the Full Sequence of 3 prime D recombination site (D-genes only)", "field": "d_rs_3_prime_end"})
    ret.items.append({"item": "d_rs_5_prime_start", "value": sub.d_rs_5_prime_start, "tooltip": "Start co-ordinate in the Full Sequence of 5 prime D recombination site (D-genes only)", "field": "d_rs_5_prime_start"})
    ret.items.append({"item": "d_rs_5_prime_end", "value": sub.d_rs_5_prime_end, "tooltip": "End co-ordinate in the Full Sequence of 5 prime D recombination site (D-genes only)", "field": "d_rs_5_prime_end"})
    ret.items.append({"item": "j_rs_start", "value": sub.j_rs_start, "tooltip": "Start co-ordinate in the Full Sequence of J recombination site (J-genes only)", "field": "j_rs_start"})
    ret.items.append({"item": "j_rs_end", "value": sub.j_rs_end, "tooltip": "End co-ordinate in the Full Sequence of J recombination site (J-genes only)", "field": "j_rs_end"})
    ret.items.append({"item": "Codon Frame", "value": sub.j_codon_frame, "tooltip": "Codon position of the first sequence symbol in the Coding Sequence. Mandatory for J genes. Not used for V or D genes. ('1' means the sequence is in-frame, '2' means that the first bp is missing from the first codon, '3' means that the first 2 bp are missing)", "field": "j_codon_frame"})
    ret.items.append({"item": "J CDR3 End", "value": sub.j_cdr3_end, "tooltip": "In the case of a J-gene, the co-ordinate in the Coding Sequence of the first nucelotide of the conserved PHE or TRP (IMGT codon position 118)", "field": "j_cdr3_end"})
    ret.items.append({"item": "Paralogs", "value": sub.paralogs, "tooltip": "Canonical names of 0 or more paralogs", "field": "paralogs"})
    ret.items.append({"item": "Extension?", "value": sub.inferred_extension, "tooltip": "Checked if the inference reports an extension to a known sequence", "field": "inferred_extension"})
    ret.items.append({"item": "3\'  Extension", "value": sub.ext_3prime, "tooltip": "Extending sequence at 3\' end (IMGT gapped)", "field": "ext_3prime"})
    ret.items.append({"item": "3\' start", "value": sub.start_3prime_ext, "tooltip": "Start co-ordinate of 3\' extension (if any) in IMGT numbering", "field": "start_3prime_ext"})
    ret.items.append({"item": "3\' end", "value": sub.end_3prime_ext, "tooltip": "End co-ordinate of 3\' extension (if any) in IMGT numbering", "field": "end_3prime_ext"})
    ret.items.append({"item": "5\' Extension", "value": sub.ext_5prime, "tooltip": "Extending sequence at 5\' end (IMGT gapped)", "field": "ext_5prime"})
    ret.items.append({"item": "5\' start", "value": sub.start_5prime_ext, "tooltip": "Start co-ordinate of 5\' extension (if any) in IMGT numbering", "field": "start_5prime_ext"})
    ret.items.append({"item": "5\' end", "value": sub.end_5prime_ext, "tooltip": "End co-ordinate of 5\' extension (if any) in IMGT numbering", "field": "end_5prime_ext"})
    ret.items.append({"item": "curational_tags", "value": sub.curational_tags, "tooltip": "Controlled-vocabulary tags applied to this description", "field": "curational_tags"})
    return ret


class GenomicSupport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sequence_type = db.Column(db.String(255))
    sequence = db.Column(db.Text())
    notes = db.Column(db.Text())
    repository = db.Column(db.String(1000))
    accession = db.Column(db.String(1000))
    patch_no = db.Column(db.String(1000))
    gff_seqid = db.Column(db.String(1000))
    sequence_start = db.Column(db.Integer)
    sequence_end = db.Column(db.Integer)
    sense = db.Column(db.String(255))
    url = db.Column(db.Text())
    sequence_id = db.Column(db.Integer, db.ForeignKey('gene_description.id'))
    gene_description = db.relationship('GeneDescription', backref = 'genomic_accessions')


def save_GenomicSupport(db, object, form, new=False):
    object.sequence_type = form.sequence_type.data
    object.sequence = form.sequence.data
    object.notes = form.notes.data
    object.repository = form.repository.data
    object.accession = form.accession.data
    object.patch_no = form.patch_no.data
    object.gff_seqid = form.gff_seqid.data
    object.sequence_start = form.sequence_start.data
    object.sequence_end = form.sequence_end.data
    object.sense = form.sense.data
    object.url = form.url.data

    if new:
        db.session.add(object)

    db.session.commit()



def populate_GenomicSupport(db, object, form):
    form.sequence_type.data = object.sequence_type
    form.sequence.data = object.sequence
    form.notes.data = object.notes
    form.repository.data = object.repository
    form.accession.data = object.accession
    form.patch_no.data = object.patch_no
    form.gff_seqid.data = object.gff_seqid
    form.sequence_start.data = object.sequence_start
    form.sequence_end.data = object.sequence_end
    form.sense.data = object.sense
    form.url.data = object.url




def copy_GenomicSupport(c_from, c_to):
    c_to.sequence_type = c_from.sequence_type
    c_to.sequence = c_from.sequence
    c_to.notes = c_from.notes
    c_to.repository = c_from.repository
    c_to.accession = c_from.accession
    c_to.patch_no = c_from.patch_no
    c_to.gff_seqid = c_from.gff_seqid
    c_to.sequence_start = c_from.sequence_start
    c_to.sequence_end = c_from.sequence_end
    c_to.sense = c_from.sense
    c_to.url = c_from.url



class GenomicSupport_table(StyledTable):
    id = Col("id", show=False)
    sequence_type = StyledCol("Type", tooltip="Locational should be used where the genomic sequence includes multiple genes, enabling the location of this gene to be determined relative to others")
    repository = StyledCol("Repository", tooltip="Name of the repository in which the assembly or sequence is deposited")
    accession = StyledCol("Accession", tooltip="Accession number of the assembly or sequence within the repository")
    sequence_start = StyledCol("Start", tooltip="start co-ordinate of the sequence of this gene in the assembly or sequence")
    sequence_end = StyledCol("End", tooltip="end co-ordinate of the sequence of this gene in the assembly or sequence")


def make_GenomicSupport_table(results, private = False, classes=()):
    t = create_table(base=GenomicSupport_table)
    ret = t(results, classes=classes)
    return ret

class GenomicSupport_view(Table):
    item = ViewCol("", column_html_attrs={"class": "col-sm-3 text-right font-weight-bold view-table-row"})
    value = Col("")


def make_GenomicSupport_view(sub, private = False):
    ret = GenomicSupport_view([])
    ret.items.append({"item": "Type", "value": sub.sequence_type, "tooltip": "Locational should be used where the genomic sequence includes multiple genes, enabling the location of this gene to be determined relative to others", "field": "sequence_type"})
    ret.items.append({"item": "Sequence", "value": sub.sequence, "tooltip": "Sequence of interest described in this record (typically this will include gene and promoter region)", "field": "sequence"})
    ret.items.append({"item": "Notes", "value": sub.notes, "tooltip": "Notes", "field": "notes"})
    ret.items.append({"item": "Repository", "value": sub.repository, "tooltip": "Name of the repository in which the assembly or sequence is deposited", "field": "repository"})
    ret.items.append({"item": "Accession", "value": sub.accession, "tooltip": "Accession number of the assembly or sequence within the repository", "field": "accession"})
    ret.items.append({"item": "Patch", "value": sub.patch_no, "tooltip": "Patch number of the assembly or sequence within the repository", "field": "patch_no"})
    ret.items.append({"item": "gff seqid", "value": sub.gff_seqid, "tooltip": "name of the chromosome or scaffold (for assemblies only)", "field": "gff_seqid"})
    ret.items.append({"item": "Start", "value": sub.sequence_start, "tooltip": "start co-ordinate of the sequence of this gene in the assembly or sequence", "field": "sequence_start"})
    ret.items.append({"item": "End", "value": sub.sequence_end, "tooltip": "end co-ordinate of the sequence of this gene in the assembly or sequence", "field": "sequence_end"})
    ret.items.append({"item": "Sense", "value": sub.sense, "tooltip": "+ (forward) or - (reverse)", "field": "sense"})
    ret.items.append({"item": "URL", "value": sub.url, "tooltip": "Link to record", "field": "url"})
    return ret

