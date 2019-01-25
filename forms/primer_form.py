
# FlaskForm class definitions for Primer
# This file is automatically generated from the schema by schema/build_from_schema.py

from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from custom_validators import *
from wtforms import StringField, SelectField, DateField, BooleanField, IntegerField, DecimalField, TextAreaField, HiddenField, validators
class PrimerForm(FlaskForm):
    primer_name = StringField('Primer Name', [validators.Length(max=255)], description="Primer name or quick description")
    primer_seq = StringField('Primer Sequence', [ValidNucleotideSequence(ambiguous=True)], description="primer sequence (may contain ambiguous characters)")


