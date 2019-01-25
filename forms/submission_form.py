
# FlaskForm class definitions for Submission
# This file is automatically generated from the schema by schema/build_from_schema.py

from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from custom_validators import *
from wtforms import StringField, SelectField, DateField, BooleanField, IntegerField, DecimalField, TextAreaField, HiddenField, validators
class SubmissionForm(FlaskForm):
    submission_id = StringField('Submission ID', [validators.Length(max=255)], description="Unique ID assigned by IARC on recipt of submission")
    submission_date = DateField('Submission Date', description="Date submission received")
    submission_status = SelectField('Submission Status', choices=[('draft', 'draft'), ('reviewing', 'reviewing'), ('published', 'published'), ('complete', 'complete')], description="Status of submission")
    submitter_name = StringField('Submitter', [validators.Length(max=255)], description="Full contact information of the submitter, i.e. the person depositing the data")
    submitter_address = StringField('Submitter Address', [validators.Length(max=255)], description="Institution and full address of submitter")
    submitter_email = StringField('Submitter Email', [validators.Length(max=255)], description="Preferred email address of submitter")
    species = SelectField('Species')
    population_ethnicity = StringField('Ethnicity', [validators.Length(max=255)], description="Information on the ethnicity/population/race of the sample from which the submitted allele was inferred (if not known, use UN)")


