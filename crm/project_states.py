from django.db import models
from django_fsm import FSMField, transition


class ProjectStateMixin(models.Model):
    state = FSMField(default='requested', editable=False)
    state_colors = {
        "requested": "#71b2d4",
        "scoped": "#43b1b0",
        "introduced": "#71b2d4",
        "signed": "#189370",
        "progress": "#43b1b0",
        "finished": "#246060",
        "stopped": "#cd3238"
    }

    @property
    def state_color(self):
        return self.state_colors.get(self.state, '#000')

    @transition(field=state, source='requested', target='scoped', custom={
        "help": "This project was scoped, on email or call",
    })
    def scope(self):
        pass

    @transition(field=state, source='scoped', target='introduced', custom={
        "help": "Introduced to the end client",
    })
    def introduce(self):
        pass

    @transition(field=state, source='introduced', target='signed', custom={
        "help": "Contract signed",
    })
    def sign(self):
        pass

    @transition(field=state, source='signed', target='progress', custom={
        "help": "Started working",
    })
    def start(self):
        pass

    @transition(field=state, source='progress', target='finished', custom={
        "help": "Finished working",
    })
    def finish(self):
        pass

    @transition(field=state, source='*', target='stopped', custom={
        "help": "Project dropped",
        "classes": ["no"],
    })
    def drop(self):
        pass

    class Meta:
        abstract = True
