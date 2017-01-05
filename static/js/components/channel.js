var app = app || {};

(function(){
    // Channel Model
    app.Channel = Backbone.Model.extend({
        defaults: {
            name: "Temp",
            image: "",
            desc: "",
            link: "",
            channel_id: "",
            tags: [],
            hidden: false,
            playlist: null
        },

        containsTerm: function(term){
            var name_has_term = this.get('name').toLowerCase().search(term) > -1;
            var desc_has_term = this.get('desc').toLowerCase().search(term) > -1;
            return (name_has_term || desc_has_term);
        },

        show: function(){
            this.set({hidden: false});
        },

        hide: function(){
            this.set({hidden: true});
        },

        setPlaylist: function(){
            self = this;
            if (this.get('playlist') == null){ // load from server if null
                var url = '/channel/playlist/' + this.get('channel_id');
                $.get(url, '', function(resp){
                    self.set({'playlist': resp.replace('http', 'https')});
                });
            };
        }
    });

    // Channel Collection
    app.ChannelList = Backbone.Collection.extend({
        model: app.Channel,
        url: '/channels/',
    });

    // Channel View
    app.ChannelView = Backbone.View.extend({
        tagName: 'span',

        template: _.template($('#content-template').html()),

        events: {
            'click .content-image': 'setPlayer',
            'click .content-desc': 'setPlayer',
            'mouseover .content-view': 'showDescription',
            'mouseout .content-view': 'hideDescription'
        },

        initialize: function(){
            _.bindAll(this, 'render', 'goToPage', 'showDescription', 'hideDescription', 'updateVisibility');
            this.model.bind('change:hidden', this.updateVisibility, this);
        },

        render: function(){
            var self = this;
            $(this.el).html( this.template( this.model.attributes ));
            _(this.model.get('tags')).each(function(tag_name){
                $('div.content-tag-list', self.el).append('<span class="tag-badge badge">'+tag_name+'</span>');
            });
            return this;
        },

        goToPage: function(){
            window.open(this.model.get('link'));
        },

        showDescription:function(){
            $('div.content-desc', this.el).css('display', 'block');
        },

        hideDescription:function(){
            $('div.content-desc', this.el).css('display', 'none');
        },

        setPlayer:function(){
            var self = this;
            app.playerView.openPlayer(self.model);
        },

        updateVisibility: function(){
            if (this.model.get('hidden')){
                this.hide();
            } else {
                this.show();
            };
        },

        hide:function(){
            $(this.el).hide();
        },

        show:function(){
            $(this.el).show();
        }
    });
})();