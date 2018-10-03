
# ORM definitions for GenotypeDescription
# This file is automatically generated from the schema by schema/build_from_schema.py

from app import db
from db.userdb import User
from db.styled_table import *
from flask_table import Table, Col, LinkCol, create_table
from db.view_table import ViewCol
from sqlalchemy.orm import backref

from db._genotype_description_db import *

class GenotypeDescription(db.Model, GenotypeDescriptionMixin):
    id = db.Column(db.Integer, primary_key=True)
    genotype_name = db.Column(db.String(1000))
    genotype_subject_id = db.Column(db.String(1000))
    genotype_biosample_ids = db.Column(db.String(255))
    submission_id = db.Column(db.Integer, db.ForeignKey('submission.id'))
    submission = db.relationship('Submission', backref = 'genotype_descriptions')
    inference_tool_id = db.Column(db.Integer, db.ForeignKey('inference_tool.id'))
    inference_tool = db.relationship('InferenceTool', backref = 'genotype_descriptions')
    genotype_file = db.Column(db.LargeBinary(length=(2**32)-1))
    genotype_filename = db.Column(db.String(1000))


def save_GenotypeDescription(db, object, form, new=False):   
    object.genotype_name = form.genotype_name.data
    object.genotype_subject_id = form.genotype_subject_id.data
    object.genotype_biosample_ids = form.genotype_biosample_ids.data
    object.inference_tool_id = form.inference_tool_id.data
    object.genotype_filename = form.genotype_filename.data

    if new:
        db.session.add(object)
        
    db.session.commit()   



def populate_GenotypeDescription(db, object, form):   
    form.genotype_name.data = object.genotype_name
    form.genotype_subject_id.data = object.genotype_subject_id
    form.genotype_biosample_ids.data = object.genotype_biosample_ids
    form.genotype_file.data = object.genotype_file
    form.genotype_filename.data = object.genotype_filename




def copy_GenotypeDescription(c_from, c_to):   
    c_to.genotype_name = c_from.genotype_name
    c_to.genotype_subject_id = c_from.genotype_subject_id
    c_to.genotype_biosample_ids = c_from.genotype_biosample_ids
    c_to.genotype_file = c_from.genotype_file
    c_to.genotype_filename = c_from.genotype_filename



class GenotypeDescription_table(StyledTable):
    id = Col("id", show=False)
    genotype_name = StyledCol("Genotype Name", tooltip="Descriptive name for this genotype")
    genotype_subject_id = StyledCol("Subject ID", tooltip="Identifier of the subject from which this genotype was inferred")
    genotype_filename = StyledCol("Genotype Filename", tooltip="Name of the uploaded file from which the genotype was read")


def make_GenotypeDescription_table(results, private = False, classes=()):
    t=create_table(base=GenotypeDescription_table)
    ret = t(results, classes=classes)
    return ret

class GenotypeDescription_view(Table):
    item = ViewCol("", column_html_attrs={"class": "col-sm-3 text-right font-weight-bold view-table-row"})
    value = Col("")


def make_GenotypeDescription_view(sub, private = False):
    ret = GenotypeDescription_view([])
    ret.items.append({"item": "Genotype Name", "value": sub.genotype_name, "tooltip": "Descriptive name for this genotype", "field": "genotype_name"})
    ret.items.append({"item": "Subject ID", "value": sub.genotype_subject_id, "tooltip": "Identifier of the subject from which this genotype was inferred", "field": "genotype_subject_id"})
    ret.items.append({"item": "Sample IDs", "value": sub.genotype_biosample_ids, "tooltip": "Comma-separated list of accession number(s) of the sample(s) from which the genotype was derived (e.g. SAMN05924304)", "field": "genotype_biosample_ids"})
    ret.items.append({"item": "Genotype Filename", "value": sub.genotype_filename, "tooltip": "Name of the uploaded file from which the genotype was read", "field": "genotype_filename"})
    return ret

