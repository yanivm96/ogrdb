
# ORM definitions for InferenceTool
from app import db
from db.userdb import User
from db.styled_table import *
from flask_table import Table, Col, LinkCol, create_table
from db.view_table import ViewCol

class InferenceTool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tool_settings_name = db.Column(db.String(255))
    tool_name = db.Column(db.String(255))
    tool_version = db.Column(db.String(255))
    tool_starting_database = db.Column(db.Text())
    tool_settings = db.Column(db.Text())
    submission_id = db.Column(db.Integer, db.ForeignKey('submission.id'))
    submission = db.relationship('Submission', backref = 'inference_tools')


def save_InferenceTool(db, object, form, new=False):   
    object.tool_settings_name = form.tool_settings_name.data
    object.tool_name = form.tool_name.data
    object.tool_version = form.tool_version.data
    object.tool_starting_database = form.tool_starting_database.data
    object.tool_settings = form.tool_settings.data

    if new:
        db.session.add(object)
        
    db.session.commit()   



def populate_InferenceTool(db, object, form):   
    form.tool_settings_name.data = object.tool_settings_name
    form.tool_name.data = object.tool_name
    form.tool_version.data = object.tool_version
    form.tool_starting_database.data = object.tool_starting_database
    form.tool_settings.data = object.tool_settings



class InferenceTool_table(StyledTable):
    id = Col("id", show=False)
    tool_settings_name = StyledCol("Tool/Settings Name", tooltip="Descriptive name for this combination of tool and settings")
    tool_name = StyledCol("Tool Name", tooltip="Name of the inference tool")
    tool_version = StyledCol("Tool Version", tooltip="Version of the inference tool")


def make_InferenceTool_table(results, private = False, classes=()):
    t=create_table(base=InferenceTool_table)
    ret = t(results, classes=classes)
    return ret

class InferenceTool_view(Table):
    item = ViewCol("", column_html_attrs={"class": "col-sm-3 text-right font-weight-bold view-table-row"})
    value = Col("")


def make_InferenceTool_view(sub, private = False):
    ret = InferenceTool_view([])
    ret.items.append({"item": "Tool/Settings Name", "value": sub.tool_settings_name, "tooltip": "Descriptive name for this combination of tool and settings"})
    ret.items.append({"item": "Tool Name", "value": sub.tool_name, "tooltip": "Name of the inference tool"})
    ret.items.append({"item": "Tool Version", "value": sub.tool_version, "tooltip": "Version of the inference tool"})
    ret.items.append({"item": "Starting Database", "value": sub.tool_starting_database, "tooltip": "Starting germline database used by the tool (please specify where and when it was obtained, name, and version id, if any)"})
    ret.items.append({"item": "Settings", "value": sub.tool_settings, "tooltip": "Settings/configuration of the tool when used to provide the inferences"})
    return ret

