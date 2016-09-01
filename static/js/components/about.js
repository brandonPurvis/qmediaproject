var app = app || {};

(function(){
    // View
    app.AboutView = Backbone.View.extend({
        el: $('#about-container'),

        template: _.template($('#about-template').html()),

        initialize: function(){
            _.bindAll(this, 'render');
            this.render();
        },

        render:function(){
            $(this.el).html(this.template());
        },

        show: function(){
            $(this.el).show();
        },

        hide: function(){
            $(this.el).hide();
        }
    });
})();
