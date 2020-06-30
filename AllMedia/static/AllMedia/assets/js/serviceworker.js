// starting js

let CacheName = 'music-plus-cache-v1'

let urlsToCache = [
	'/',
	'/static/AllMedia/assets/css/musicBox.css',
	'/templates/AllMedia/delete_confirm.html',
	'/static/AllMedia/assets/css/delete_confirm.css',
]

self.addEventListener('install', function(event){
	// install steps
	event.waitUntill(
		caches.open(CacheName)
		.then(function(cache){
			console.log('opened cached');
			return cache.addAll(urlsToCache);
		})

	);
});	


self.addEventListener('fetch', function(event){
	event.respondWith(
			caches.match(event.request).then(function(response){
				return fetch(event.request)
				.catch(function(rsp){
					return response;
				});
			})
		);
});