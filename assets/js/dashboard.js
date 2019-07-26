---
---
require.config({
    shim: {
        'bootstrap': ['jquery'],
        'core': ['bootstrap', 'jquery'],
    },
    paths: {
        'bootstrap': 'assets/js/vendors/bootstrap.bundle.min',
        'circle-progress': 'assets/js/vendors/circle-progress.min',
        'core': 'assets/js/core',
        'jquery': 'assets/js/vendors/jquery-3.2.1.min',
        'selectize': 'assets/js/vendors/selectize.min',
    }
});

window.tabler = {
    colors: {
        {% for color in site.colors %}
        '{{ color[0] }}': '{{ color[1].hex }}',
        '{{ color[0] }}-darkest': '{{ color[1].hex | mix: "#000000", 20  }}',
        '{{ color[0] }}-darker': '{{ color[1].hex | mix: "#000000", 40  }}',
        '{{ color[0] }}-dark': '{{ color[1].hex | mix: "#000000", 80  }}',
        '{{ color[0] }}-light': '{{ color[1].hex | mix: "#ffffff", 70 }}',
        '{{ color[0] }}-lighter': '{{ color[1].hex | mix: "#ffffff", 30 }}',
        '{{ color[0] }}-lightest': '{{ color[1].hex | mix: "#ffffff", 10 }}'{% unless forloop.last %},{% endunless %}{% endfor %}
    }
};

require(['core']);