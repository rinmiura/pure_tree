from django.template import Library
from django.utils.html import mark_safe
from django.db.models import Aggregate, CharField, Count
from django.contrib.postgres.aggregates import StringAgg

from app.models import Menu


register = Library()


@register.simple_tag
def draw_menu(current):
    nodes = get_nodes_for_current(current)
    queryset = get_queryset(nodes)
    return render_tree(nodes, queryset)


def render_tree(nodes, queryset):
    _iter = iter(queryset)
    nodes.remove('None')
    return mark_safe(get_html_tree(nodes, _iter))


def get_html_tree(nodes, __iter_queryset, urls=None):
    if urls is None:
        urls = {}
    try:
        _set = next(__iter_queryset)
    except StopIteration:
        return ''
    html = '<ul>'
    for _node in _set['names'].split(','):
        urls[_node] = urls.get(_set['parent'], '/') + _node + '/'
        html += '<li><a href="%s">%s</a></li>' % (urls[_node], _node)
        if _node in nodes:
            nodes.remove(_node)
            html += get_html_tree(nodes, __iter_queryset, urls)
    html += '</ul>'
    return html


def get_queryset(nodes):
    queryset = []
    for obj in Menu.objects.values('parent').\
            annotate(
                count=Count('parent'),
                names=StringAgg('name', delimiter=',')
            ).order_by('parent'):
        if obj['parent'] in nodes:
            obj.update(depth=nodes.index(obj['parent']))
            queryset.append(obj)
    queryset = sorted(queryset, key=lambda d: d['depth'])
    return queryset


def get_nodes_for_current(current):
    current = 'None' + current
    nodes = list(filter(lambda x: x, current.split('/')))
    return nodes
