
# ORM definitions for Submission
# This file is automatically generated from the schema by schema/build_from_schema.py

from app import db
from db.userdb import User
from db.styled_table import *
from flask_table import Table, Col, LinkCol, create_table
from db.view_table import ViewCol
from sqlalchemy.orm import backref

from db._submission_db import *

class Submission(db.Model, SubmissionMixin):
    id = db.Column(db.Integer, primary_key=True)
    submission_id = db.Column(db.String(1000))
    submission_date = db.Column(db.DateTime)
    submission_status = db.Column(db.String(255))
    public = db.Column(db.Boolean)
    submitter_name = db.Column(db.String(1000))
    submitter_address = db.Column(db.String(1000))
    submitter_email = db.Column(db.String(255))
    species = db.Column(db.String(255))
    population_ethnicity = db.Column(db.String(1000))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    owner = db.relationship('User', backref = 'submissions')


def save_Submission(db, object, form, new=False):   
    object.submission_id = form.submission_id.data
    object.submission_date = form.submission_date.data
    object.submission_status = form.submission_status.data
    object.submitter_name = form.submitter_name.data
    object.submitter_address = form.submitter_address.data
    object.submitter_email = form.submitter_email.data
    object.species = form.species.data
    object.population_ethnicity = form.population_ethnicity.data

    if new:
        db.session.add(object)
        
    db.session.commit()   



def populate_Submission(db, object, form):   
    form.submission_id.data = object.submission_id
    form.submission_date.data = object.submission_date
    form.submission_status.data = object.submission_status
    form.submitter_name.data = object.submitter_name
    form.submitter_address.data = object.submitter_address
    form.submitter_email.data = object.submitter_email
    form.species.data = object.species
    form.population_ethnicity.data = object.population_ethnicity




def copy_Submission(c_from, c_to):   
    c_to.submission_id = c_from.submission_id
    c_to.submission_date = c_from.submission_date
    c_to.submission_status = c_from.submission_status
    c_to.public = c_from.public
    c_to.submitter_name = c_from.submitter_name
    c_to.submitter_address = c_from.submitter_address
    c_to.submitter_email = c_from.submitter_email
    c_to.species = c_from.species
    c_to.population_ethnicity = c_from.population_ethnicity



class Submission_table(StyledTable):
    id = Col("id", show=False)
    submission_id = StyledCol("Submission ID", tooltip="Unique ID assigned by IARC on recipt of submission")
    submission_date = StyledCol("Submission Date", tooltip="Date submission received")
    submission_status = StyledCol("Submission Status", tooltip="Status of submission")
    submitter_name = StyledCol("Submitter", tooltip="Full contact information of the submitter, i.e. the person depositing the data")
    species = StyledCol("Species", tooltip="Binomial designation of subject's species")


def make_Submission_table(results, private = False, classes=()):
    t=create_table(base=Submission_table)
    ret = t(results, classes=classes)
    return ret

class Submission_view(Table):
    item = ViewCol("", column_html_attrs={"class": "col-sm-3 text-right font-weight-bold view-table-row"})
    value = Col("")


def make_Submission_view(sub, private = False):
    ret = Submission_view([])
    ret.items.append({"item": "Submission ID", "value": sub.submission_id, "tooltip": "Unique ID assigned by IARC on recipt of submission", "field": "submission_id"})
    ret.items.append({"item": "Submission Date", "value": sub.submission_date, "tooltip": "Date submission received", "field": "submission_date"})
    ret.items.append({"item": "Submission Status", "value": sub.submission_status, "tooltip": "Status of submission", "field": "submission_status"})
    ret.items.append({"item": "Submitter", "value": sub.submitter_name, "tooltip": "Full contact information of the submitter, i.e. the person depositing the data", "field": "submitter_name"})
    ret.items.append({"item": "Submitter Address", "value": sub.submitter_address, "tooltip": "Institution and full address of submitter", "field": "submitter_address"})
    if private:
        ret.items.append({"item": "Submitter Email", "value": sub.submitter_email, "tooltip": "Preferred email address of submitter", "field": "submitter_email"})
    ret.items.append({"item": "Species", "value": sub.species, "tooltip": "Binomial designation of subject's species", "field": "species"})
    ret.items.append({"item": "Ethnicity", "value": sub.population_ethnicity, "tooltip": "Information on the ethnicity/population/race of the sample from which the submitted allele was inferred (if not known, use UN)", "field": "population_ethnicity"})
    return ret

