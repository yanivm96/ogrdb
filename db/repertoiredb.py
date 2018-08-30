
# ORM definitions for PubId
from app import db
from db.userdb import User
from db.styled_table import *
from flask_table import Table, Col, LinkCol, create_table
from db.view_table import ViewCol

class PubId(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pubmed_id = db.Column(db.String(255))
    pub_title = db.Column(db.String(255))
    pub_authors = db.Column(db.String(255))
    repertoire_id = db.Column(db.Integer, db.ForeignKey('repertoire.id'))
    repertoire = db.relationship('Repertoire', backref = 'pub_ids')


def save_PubId(db, object, form, new=False):   
    object.pubmed_id = form.pubmed_id.data

    if new:
        db.session.add(object)
        
    db.session.commit()   



def populate_PubId(db, object, form):   
    form.pubmed_id.data = object.pubmed_id



class PubId_table(StyledTable):
    id = Col("id", show=False)
    pubmed_id = StyledCol("PubMed ID", tooltip="PubMed ID (e.g. 26543)")
    pub_title = StyledCol("Title", tooltip="Publication Title")
    pub_authors = StyledCol("Authors", tooltip="Author list")


def make_PubId_table(results, private = False, classes=()):
    t=create_table(base=PubId_table)
    ret = t(results, classes=classes)
    return ret

class PubId_view(Table):
    item = ViewCol("", column_html_attrs={"class": "col-sm-3 text-right font-weight-bold view-table-row"})
    value = Col("")


def make_PubId_view(sub, private = False):
    ret = PubId_view([])
    ret.items.append({"item": "PubMed ID", "value": sub.pubmed_id, "tooltip": "PubMed ID (e.g. 26543)"})
    return ret


class ForwardPrimer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fw_primer_name = db.Column(db.String(255))
    fw_primer_seq = db.Column(db.String(1000))
    repertoire_id = db.Column(db.Integer, db.ForeignKey('repertoire.id'))
    repertoire = db.relationship('Repertoire', backref = 'forward_primer_set')


def save_ForwardPrimer(db, object, form, new=False):   
    object.fw_primer_name = form.fw_primer_name.data
    object.fw_primer_seq = form.fw_primer_seq.data

    if new:
        db.session.add(object)
        
    db.session.commit()   



def populate_ForwardPrimer(db, object, form):   
    form.fw_primer_name.data = object.fw_primer_name
    form.fw_primer_seq.data = object.fw_primer_seq



class ForwardPrimer_table(StyledTable):
    id = Col("id", show=False)
    fw_primer_name = StyledCol("Primer Name", tooltip="Primer name or quick description")
    fw_primer_seq = StyledCol("Primer Sequence", tooltip="primer sequence (may contain ambiguous characters)")


def make_ForwardPrimer_table(results, private = False, classes=()):
    t=create_table(base=ForwardPrimer_table)
    ret = t(results, classes=classes)
    return ret

class ForwardPrimer_view(Table):
    item = ViewCol("", column_html_attrs={"class": "col-sm-3 text-right font-weight-bold view-table-row"})
    value = Col("")


def make_ForwardPrimer_view(sub, private = False):
    ret = ForwardPrimer_view([])
    ret.items.append({"item": "Primer Name", "value": sub.fw_primer_name, "tooltip": "Primer name or quick description"})
    ret.items.append({"item": "Primer Sequence", "value": sub.fw_primer_seq, "tooltip": "primer sequence (may contain ambiguous characters)"})
    return ret


class ReversePrimer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rv_primer_name = db.Column(db.String(255))
    rv_primer_seq = db.Column(db.String(1000))
    repertoire_id = db.Column(db.Integer, db.ForeignKey('repertoire.id'))
    repertoire = db.relationship('Repertoire', backref = 'reverse_primer_set')


def save_ReversePrimer(db, object, form, new=False):   
    object.rv_primer_name = form.rv_primer_name.data
    object.rv_primer_seq = form.rv_primer_seq.data

    if new:
        db.session.add(object)
        
    db.session.commit()   



def populate_ReversePrimer(db, object, form):   
    form.rv_primer_name.data = object.rv_primer_name
    form.rv_primer_seq.data = object.rv_primer_seq



class ReversePrimer_table(StyledTable):
    id = Col("id", show=False)
    rv_primer_name = StyledCol("Primer Name", tooltip="Primer name or quick description")
    rv_primer_seq = StyledCol("Primer Sequence", tooltip="primer sequence (may contain ambiguous characters)")


def make_ReversePrimer_table(results, private = False, classes=()):
    t=create_table(base=ReversePrimer_table)
    ret = t(results, classes=classes)
    return ret

class ReversePrimer_view(Table):
    item = ViewCol("", column_html_attrs={"class": "col-sm-3 text-right font-weight-bold view-table-row"})
    value = Col("")


def make_ReversePrimer_view(sub, private = False):
    ret = ReversePrimer_view([])
    ret.items.append({"item": "Primer Name", "value": sub.rv_primer_name, "tooltip": "Primer name or quick description"})
    ret.items.append({"item": "Primer Sequence", "value": sub.rv_primer_seq, "tooltip": "primer sequence (may contain ambiguous characters)"})
    return ret


class Acknowledgements(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ack_name = db.Column(db.String(255))
    ack_institution_name = db.Column(db.String(255))
    ack_ORCID_id = db.Column(db.String(255))
    submission_id = db.Column(db.Integer, db.ForeignKey('submission.id'))
    submission = db.relationship('Submission', backref = 'acknowledgements')


def save_Acknowledgements(db, object, form, new=False):   
    object.ack_name = form.ack_name.data
    object.ack_institution_name = form.ack_institution_name.data
    object.ack_ORCID_id = form.ack_ORCID_id.data

    if new:
        db.session.add(object)
        
    db.session.commit()   



def populate_Acknowledgements(db, object, form):   
    form.ack_name.data = object.ack_name
    form.ack_institution_name.data = object.ack_institution_name
    form.ack_ORCID_id.data = object.ack_ORCID_id



class Acknowledgements_table(StyledTable):
    id = Col("id", show=False)
    ack_name = StyledCol("Name", tooltip="Name of individual to be acknowledged as contributing to this work")
    ack_institution_name = StyledCol("Institution", tooltip="Individual's department and institution name")
    ack_ORCID_id = StyledCol("ORCID ID", tooltip="Individual's ORCID Id, if available")


def make_Acknowledgements_table(results, private = False, classes=()):
    t=create_table(base=Acknowledgements_table)
    ret = t(results, classes=classes)
    return ret

class Acknowledgements_view(Table):
    item = ViewCol("", column_html_attrs={"class": "col-sm-3 text-right font-weight-bold view-table-row"})
    value = Col("")


def make_Acknowledgements_view(sub, private = False):
    ret = Acknowledgements_view([])
    ret.items.append({"item": "Name", "value": sub.ack_name, "tooltip": "Name of individual to be acknowledged as contributing to this work"})
    ret.items.append({"item": "Institution", "value": sub.ack_institution_name, "tooltip": "Individual's department and institution name"})
    ret.items.append({"item": "ORCID ID", "value": sub.ack_ORCID_id, "tooltip": "Individual's ORCID Id, if available"})
    return ret


class Repertoire(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    repository_name = db.Column(db.String(255))
    repository_id = db.Column(db.String(255))
    dataset_url = db.Column(db.String(255))
    miarr_compliant = db.Column(db.String(255))
    miairr_link = db.Column(db.String(255))
    sequencing_platform = db.Column(db.String(255))
    read_length = db.Column(db.String(255))
    primers_overlapping = db.Column(db.String(255))
    submission_id = db.Column(db.Integer, db.ForeignKey('submission.id'))
    submission = db.relationship('Submission', backref = 'repertoire')


def save_Repertoire(db, object, form, new=False):   
    object.repository_name = form.repository_name.data
    object.repository_id = form.repository_id.data
    object.dataset_url = form.dataset_url.data
    object.miarr_compliant = form.miarr_compliant.data
    object.miairr_link = form.miairr_link.data
    object.sequencing_platform = form.sequencing_platform.data
    object.read_length = form.read_length.data
    object.primers_overlapping = form.primers_overlapping.data

    if new:
        db.session.add(object)
        
    db.session.commit()   



def populate_Repertoire(db, object, form):   
    form.repository_name.data = object.repository_name
    form.repository_id.data = object.repository_id
    form.dataset_url.data = object.dataset_url
    form.miarr_compliant.data = object.miarr_compliant
    form.miairr_link.data = object.miairr_link
    form.sequencing_platform.data = object.sequencing_platform
    form.read_length.data = object.read_length
    form.primers_overlapping.data = object.primers_overlapping



class Repertoire_table(StyledTable):
    id = Col("id", show=False)


def make_Repertoire_table(results, private = False, classes=()):
    t=create_table(base=Repertoire_table)
    ret = t(results, classes=classes)
    return ret

class Repertoire_view(Table):
    item = ViewCol("", column_html_attrs={"class": "col-sm-3 text-right font-weight-bold view-table-row"})
    value = Col("")


def make_Repertoire_view(sub, private = False):
    ret = Repertoire_view([])
    ret.items.append({"item": "Repository", "value": sub.repository_name, "tooltip": "Name of the repository holding the sequence dataset (e.g. NIH SRA, or ENA)"})
    ret.items.append({"item": "Accession Number", "value": sub.repository_id, "tooltip": "Accession number or serial number within the repository (e.g. NIH Project or ENA Study)"})
    ret.items.append({"item": "Dataset URL", "value": sub.dataset_url, "tooltip": "URL of the study or project within the repository"})
    ret.items.append({"item": "MiAIRR Compliant?", "value": sub.miarr_compliant, "tooltip": "Yes if the repertoire dataset and associated metadata is available in MiAIRR format"})
    ret.items.append({"item": "MiAIRR URL", "value": sub.miairr_link, "tooltip": "Link to MiAIRR metadata, if available"})
    ret.items.append({"item": "Sequencing Platform", "value": sub.sequencing_platform, "tooltip": "Designation of sequencing instrument used"})
    ret.items.append({"item": "Read Length", "value": sub.read_length, "tooltip": "Read length in bases for each direction"})
    ret.items.append({"item": "Primers Overlapping?", "value": sub.primers_overlapping, "tooltip": "Do primers overlap with the stated sequence of any inferred allele?"})
    return ret

