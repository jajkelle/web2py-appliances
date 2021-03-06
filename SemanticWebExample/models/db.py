#########################################################################
## This scaffolding model makes your app work on Google App Engine too
#########################################################################

if request.env.web2py_runtime_gae: # if running on Google App Engine
    from gluon.contrib.gql import *  
    ### connect to Google BigTable
    db = GQLDB()
    ## and store sessions and tickets there
    session.connect(request, response, db=db)
    ### or use the following lines to store sessions in Memcache
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db=MEMDB(Client()))
else: # else use a normal relational database
    # if not, use SQLite or other DB
    db = DAL('sqlite://storage.sqlite')  


#########################################################################
## uncomment the following line if you do not want sessions
#session.forget()
#########################################################################

#########################################################################
## Define your tables below, for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytbale.myfield=='value).select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################


#########################################################################
## Here is sample code if you need:
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - crud actions
## comment/uncomment as needed
#########################################################################

from gluon.tools import *
auth=Auth(globals(),db)            # authentication/authorization
auth.define_tables()               # creates all needed tables
crud=Crud(globals(),db)            # for CRUD helpers using auth
service=Service(globals())         # for json, xml, jsonrpc, xmlrpc, amfrpc

## uncomment as necessary or consult docs for more options
#crud.settings.auth=auth           # (optional) enforces authorization on crud
#mail=Mail()                                  # mailer
#mail.settings.server='smtp.gmail.com:587'    # your SMTP server
#mail.settings.sender='you@gmail.com'         # your email
#mail.settings.login='username:password'      # your credentials
#auth.settings.mailer=mail         # for user email verification
#auth.settings.registration_requires_verification = True
#auth.settings.registration_requires_approval = True
#auth.messages.verify_email = \
#  'Click on the link http://.../verify_email/%(key)s to verify your email'
