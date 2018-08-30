
# FlaskForm class definitions for PubId

from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from customvalidators import *
from wtforms import StringField, SelectField, DateField, BooleanField, IntegerField, DecimalField, TextAreaField, validators
class PubIdForm(FlaskForm):
    pubmed_id = StringField('PubMed ID', [validators.Length(max=255)], description="PubMed ID (e.g. 26543)")



# FlaskForm class definitions for ForwardPrimer

from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from customvalidators import *
from wtforms import StringField, SelectField, DateField, BooleanField, IntegerField, DecimalField, TextAreaField, validators
class ForwardPrimerForm(FlaskForm):
    fw_primer_name = StringField('Primer Name', [validators.Length(max=255)], description="Primer name or quick description")
    fw_primer_seq = StringField('Primer Sequence', [ValidNucleotideSequence(ambiguous=True)], description="primer sequence (may contain ambiguous characters)")



# FlaskForm class definitions for ReversePrimer

from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from customvalidators import *
from wtforms import StringField, SelectField, DateField, BooleanField, IntegerField, DecimalField, TextAreaField, validators
class ReversePrimerForm(FlaskForm):
    rv_primer_name = StringField('Primer Name', [validators.Length(max=255)], description="Primer name or quick description")
    rv_primer_seq = StringField('Primer Sequence', [ValidNucleotideSequence(ambiguous=True)], description="primer sequence (may contain ambiguous characters)")



# FlaskForm class definitions for Acknowledgements

from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from customvalidators import *
from wtforms import StringField, SelectField, DateField, BooleanField, IntegerField, DecimalField, TextAreaField, validators
class AcknowledgementsForm(FlaskForm):
    ack_name = StringField('Name', [validators.Length(max=255)], description="Name of individual to be acknowledged as contributing to this work")
    ack_institution_name = StringField('Institution', [validators.Length(max=255)], description="Individual's department and institution name")
    ack_ORCID_id = StringField('ORCID ID', [validators.Optional(), ValidOrcidID()], description="Individual's ORCID Id, if available")



# FlaskForm class definitions for Repertoire

from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from customvalidators import *
from wtforms import StringField, SelectField, DateField, BooleanField, IntegerField, DecimalField, TextAreaField, validators
class RepertoireForm(FlaskForm):
    repository_name = StringField('Repository', [validators.Length(max=255)], description="Name of the repository holding the sequence dataset (e.g. NIH SRA, or ENA)")
    repository_id = StringField('Accession Number', [validators.Length(max=255)], description="Accession number or serial number within the repository (e.g. NIH Project or ENA Study)")
    dataset_url = StringField('Dataset URL', [validators.Length(max=255)], description="URL of the study or project within the repository")
    miarr_compliant = SelectField('MiAIRR Compliant?', choices=[('Yes', 'Yes'), ('No', 'No')], description="Yes if the repertoire dataset and associated metadata is available in MiAIRR format")
    miairr_link = StringField('MiAIRR URL', [validators.Length(max=255)], description="Link to MiAIRR metadata, if available")
    sequencing_platform = StringField('Sequencing Platform', [validators.Length(max=255)], description="Designation of sequencing instrument used")
    read_length = StringField('Read Length', [validators.Length(max=255)], description="Read length in bases for each direction")
    primers_overlapping = SelectField('Primers Overlapping?', choices=[('Yes', 'Yes'), ('No', 'No')], description="Do primers overlap with the stated sequence of any inferred allele?")


