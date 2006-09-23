
from django import template
from datetime import datetime

register = template.Library()

def form_spacer():
    return '<div class="form_spacer"></div>'

def form_label(label, idfor='foo'):
    return '<label for="id_%s">%s:</label><br>\n' % (idfor, label)


def form_input_text(label, name, value, size='big'):
    out = form_label(label, name)
    out += '<input type="text" name="'+name+'" id="id_'+name+'" class="input_standard width_'+size+'" value="'+value+'">\n'
    return out

def form_select_without_label(name, options, selected):
    out = '<select name="%s">\n' % name
    for (opt_value,opt_label) in options:
        out += '<option value="%s"' % opt_value
        if opt_value == selected:
            out += ' selected="selected"'
        out += '>%s</option>\n' % opt_label
    out += '</select>'
    return out


def form_select(label, name, options, selected):
    out = form_label(label, name)
    out += form_select_without_label(name, options, selected)
    return out


def form_select_date(label, prefix, date, startyear=1940, endyear=datetime.now().year+5):
    days = [(x+1 ,"%02d" % (x+1)) for x in range(31)]
    months = [(x+1, "%02d" % (x+1)) for x in range(12)]
    years = [(x+startyear,x+startyear) for x in range(endyear-startyear+1)]
    
    out = '<label >%s:</label><br>\n' % label
    # dzien
    out += form_select_without_label(prefix+'_day', days, date.day) + '&nbsp;'
    out += form_select_without_label(prefix+'_month', months, date.month) + '&nbsp;'
    out += form_select_without_label(prefix+'_year', years, date.year)
    return out


def form_input_check(label, name, checked):
    out = '<input type="checkbox" name="%s" value="1" id="id_%s"' % (name, name)
    if checked:
        out += ' checked="checked" '
    out += '/>&nbsp; <label for="id_%s">%s</label>' % (name, label)
    return out


def form_input_passwd(label, name, name_other=None):
    out = form_label(label, name)
    out += '<input type="password" name="%s" id="id_%s" class="input_standard width_normal" value="">' % (name, name)
    if name_other:
        out += '&nbsp; <a href="#" onclick="genPass(\'id_%s\', \'id_%s\'); return false;" class="nav">Generuj</a> &nbsp; <span id="id_gen_pass"></span>' % (name, name_other)

    return out

def form_input_textarea(label, name, value):
    out = form_label(label, name)
    out += '<textarea name="%s" id="id_%s" class="description">%s</textarea>\n' % (name, name, value)
    return out


def email(email, label=None):
    if not label:
        label = email
    return '<a href="mailto:%s">%s</a>' % (email, label)


register.simple_tag(form_spacer)
register.simple_tag(form_input_text)
register.simple_tag(form_select)
register.simple_tag(form_select_date)
register.simple_tag(form_input_check)
register.simple_tag(form_input_passwd)
register.simple_tag(form_input_textarea)
register.simple_tag(email)
