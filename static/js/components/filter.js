var app = app || {};

(function(){

    // Model
    app.Filter = Backbone.Model.extend({
        defaults: {
            name: 'filter',
            term: ''
        }
    });

    // Collection
    app.FilterList =  Backbone.Collection.extend({
        model: app.Filter,
        url: '/filters/'
    });

    // View
    app.FilterView = Backbone.View.extend({
        tagName: 'span',

        events: {
            'click button.filter-button': 'doFilter'
        },

        initialize: function(){
            _.bindAll(this, 'render', 'doFilter');
        },

        render: function(){
            $(this.el).html('<button class="filter-button btn btn-default">'+this.model.get('name')+'</button>');
            return this;
        },

        doFilter: function(){
            this.trigger("filterChange", this.model);
        }
    });

})();