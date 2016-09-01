var app = app || {};

(function(){
    app.MenuView = Backbone.View.extend({
        el: $('#menu-container'),

        template: _.template($('#menu-template').html()),

        events: {
            'click li#home-nav': 'goToHome',
            'click li#about-nav': 'goToAbout'
        },

        initialize: function(){
            _.bindAll(this, 'render');
            this.render();
        },

        render: function(){
            $(this.el).html( this.template() );
        },

        goToHome: function(){
            app.aboutView.hide();
            app.appView.show();
        },

        goToAbout: function(){
            app.aboutView.show();
            app.appView.hide();
        }
    });
})();