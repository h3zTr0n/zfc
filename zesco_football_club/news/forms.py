from __future__ import absolute_import

from .models import Ticket
from django import forms




from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field, HTML, Row

# class TicketForm(forms.ModelForm):
#
#     class Meta:
#         model = Ticket
#         exclude = ['timestamp']
#
#     def __init__(self, *args, **kwargs):
#         super(TicketForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             Fieldset(
#             'first_name',
#             'last_name',
#             'email_address',
#             'mobile',
#             'birthday',
#             'house_number',
#             'address_one',
#             'address_two',
#             'town_city',
#             'postcode',
#             'country',
#             'priority_deposit',
#             'number_of_seats',
#             'timestamp',
#             ),
#             ButtonHolder(
#                 Submit('submit', 'Submit', css_class='button warning')
#             )
#         )
#
#     def save(self):
#         ticket = super(TicketForm, self).save(commit=False)
#         if form.is_valid():
#             ticket.save()
#         return ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = ['timestamp']

    def __init__(self, *args, **kwargs):

        super(TicketForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.form_action = 'Buy Ticket (s)'
        self.helper.layout = Layout(
            HTML("""<h3>Buy Ticket (s)</h3>"""),
            Field('first_name'),
            Field('last_name'),
            Field('email'),
            Field('mobile'),
            Field('birthday'),
            Field('house_number'),
            Field('address'),
            Field('town_city'),
            Field('postcode'),
            Field('country'),
            Field('priority_deposit'),
            Field('number_of_seats'),
        )


        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('Submit', 'Submit', css_class='button warning') )

    def save(self):
        ticket = super(TicketForm, self).save(commit=False)
        ticket.save()
        return ticket
        # self.request = kwargs.pop('request', None)
        # return super(TicketForm, self).__init__(*args, **kwargs)
