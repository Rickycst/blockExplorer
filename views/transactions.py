from flask import render_template
from flask import request

from src.eth import  eth


def render_transaction_view(id):
    _eth = eth()
    id = request.args.get("id")
    print(id)
    

    if id != None:
        print(_eth.get_transaction( id))
        return render_template('transaction.html', blockInfo={})
    else:
        return render_template('transaction.html',)