
# ORM definitions for Submission
from app import db
from db.userdb import User
from db.styled_table import *
from flask_table import Table, Col, LinkCol, create_table
from db.view_table import ViewCol

class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    submission_id = db.Column(db.String(255))
    submission_date = db.Column(db.Date)
    submission_status = db.Column(db.String(255))
    submitter_name = db.Column(db.String(255))
    submitter_address = db.Column(db.String(255))
    submitter_email = db.Column(db.String(255))
    submitter_phone = db.Column(db.String(255))
    species = db.Column(db.String(255))
    population_ethnicity = db.Column(db.String(255))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    owner = db.relationship('User', backref = 'submissions')
    from db._submissionrights import can_see, can_edit


def save_Submission(db, object, form, new=False):   
    object.submission_id = form.submission_id.data
    object.submission_date = form.submission_date.data
    object.submission_status = form.submission_status.data
    object.submitter_name = form.submitter_name.data
    object.submitter_address = form.submitter_address.data
    object.submitter_email = form.submitter_email.data
    object.submitter_phone = form.submitter_phone.data
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
    form.submitter_phone.data = object.submitter_phone
    form.species.data = object.species
    form.population_ethnicity.data = object.population_ethnicity



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
    ret.items.append({"item": "Submission ID", "value": sub.submission_id, "tooltip": "Unique ID assigned by IARC on recipt of submission"})
    ret.items.append({"item": "Submission Date", "value": sub.submission_date, "tooltip": "Date submission received"})
    ret.items.append({"item": "Submission Status", "value": sub.submission_status, "tooltip": "Status of submission"})
    ret.items.append({"item": "Submitter", "value": sub.submitter_name, "tooltip": "Full contact information of the submitter, i.e. the person depositing the data"})
    ret.items.append({"item": "Submitter Address", "value": sub.submitter_address, "tooltip": "Institutional address of submitter"})
    if private:
        ret.items.append({"item": "Submitter Email", "value": sub.submitter_email, "tooltip": "Preferred email address of submitter"})
    if private:
        ret.items.append({"item": "Submitter Phone", "value": sub.submitter_phone, "tooltip": "Preferred phone number of submitter"})
    ret.items.append({"item": "Species", "value": sub.species, "tooltip": "Binomial designation of subject's species"})
    ret.items.append({"item": "Ethnicity", "value": sub.population_ethnicity, "tooltip": "Information on the ethnicity/population/race of the sample from which the submitted allele was inferred (if not known, use UN)"})
    return ret

