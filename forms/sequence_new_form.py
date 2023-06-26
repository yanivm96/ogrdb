# Copyright William Lees
#
# This source code, and any executable file compiled or derived from it, is governed by the European Union Public License v. 1.2,
# the English version of which is available here: https://perma.cc/DK5U-NDVE
#

from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from custom_validators import *
from wtforms import SelectField, SubmitField, StringField, validators


class NewSequenceForm(FlaskForm):
    new_name = StringField('New Sequence Name', description="The name for this new sequence")
    species_subgroup = StringField('Species Subgroup', description="Species subgroup for this new sequence, if any")
    submission_id = SelectField('Submission ID', description="Inference study on which this new sequence is based")
    sequence_name = SelectField('Sequence', description="Inferred sequence on which this new sequence is based")
    upload_file = FileField('Sequence File', description="CSV file containing sequence metadata")
    evidence_file = FileField('Evidence File', description="CSV file containing sequence metadata")
    create = SubmitField('Create')
    cancel = SubmitField('Cancel')
