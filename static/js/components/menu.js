var app = app || {};

(function(){
    app.MenuView = Backbone.View.extend({
        el: $('#menu-container'),

        template: _.template($('#menu-template').html()),

        events: {
            'click li#home-nav': 'goToHome',
            'click li#about-nav': 'goToAbout',
            'click li#random-nav': 'openRandomVideo'
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
        },

        openRandomVideo: function(){
            this.hideAll();
            app.appView.show(); // Show main app view
            $.get('/channel/random/', '', function(resp){
                console.log("pl: " + resp);
                var channel = new app.Channel(resp);
                console.log("phc: " + channel);
                app.playerView.openPlayer(channel);
                app.playerView.show();
            });
        }
    });
})();