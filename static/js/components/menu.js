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

        hideAll: function(){
            app.appView.hide();
            app.aboutView.hide();
        },

        goToHome: function(){
            this.hideAll();
            app.appView.show();
        },

        goToAbout: function(){
            this.hideAll();
            app.aboutView.show();
        }
    });
})();