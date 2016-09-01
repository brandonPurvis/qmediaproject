var app = app || {};

(function(){
    app.AppView = Backbone.View.extend({
        el: $('#app-container'),

        template: _.template($('#app-template').html()),

        initialize: function(){
            var self = this;
            _.bindAll(this, 'render', 'appendContent', 'appendAllContent', 'appendFilter', 'appendAllFilter', 'filterContent');
            app.channelList.bind('add', this.appendContent, this);
            app.channelList.bind('refresh', this.appendAllContent, this);
            app.filterList.bind('add', this.appendFilter, this);
            app.filterList.bind('refresh', this.appendAllFilter, this);
            this.render();
        },

        render: function(){
            var self = this;
            $(this.el).html(this.template());
            _(app.channelList.models).each(function(item){
                self.appendItem(item);
            }, this);
        },

        appendContent: function(item){
            var channelView = new app.ChannelView({
                model: item
            });
            $('div#content', this.el).append(channelView.render().el);
        },

        appendAllContent: function(){
            var self = this;
            $('#loading-overlay').fadeOut();
            _(app.channelList.models).each(function(channel){
                self.appendContent(channel);
            });
        },

        appendFilter: function(filter){
            var filterView = new app.FilterView({
                model: filter
            });

            filterView.bind('filterChange', this.filterContent, this);
            $('div#filter', this.el).append(filterView.render().el);
        },

        appendAllFilter: function(){
            var self = this;
            _(app.filterList.models).each(function(filter){
                self.appendFilter(filter);
            });
        },

        filterContent: function(filter){
            var term = filter.get('term');
            _(app.channelList.models).each(function(channel){
                if (channel.containsTerm(term)){
                    channel.show();
                } else {
                    channel.hide();
                };
            });
        },

        show: function(){
            $(this.el).show();
        },

        hide: function(){
            $(this.el).hide();
        }
    });
})();