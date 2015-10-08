# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import ModelSQL, ModelView, fields

__all__ = ['Configuration']


class Configuration(ModelSQL, ModelView):
    'Activity Configuration'
    __name__ = 'activity.configuration'
    activity_sequence =  fields.Property(fields.Many2One('ir.sequence',
            'Activity Sequence', required=True,
            domain=[
                ('code', '=', 'activity.activity'),
                ]))
