'use strict'

var rdigestapp = angular.module('rdigestApp', []);

rdigestapp.controller('RDigestCtrl', function($scope, $http){
	$http.get('/api/links').
		then(function(response){
			$scope.data = response.data.data;
			
			var cf = crossfilter($scope.data);
			var dateDim = cf.dimension(function(d){ return d.created_utc; }); //dimension by created_utc
			var dateGroup = dateDim.group();	//group date dimension
			var dates = dateGroup.all();	// get all dates
			var postDim = cf.dimension(function(d){ return d; }) //template dimension by post

			var posts = {};
			var datestrings = {};
			dates.forEach(function(date){
				var f = postDim.filter( //filter the date by the key, grouping them together
					function(d){ 
						if(d.created_utc == date.key){
							return d;
						}
					});
				var entries = f.top(Number.POSITIVE_INFINITY);
				var dateD = new Date(date.key)
				posts[date.key] = {"entries": entries, "datestring": dateD.toDateString()}
				//posts[date.key] = f.top(5);
				//datestrings[date.key] = dateD.toDateString()//{"DAY": dateD.getDay(), "MONTH": dateD.getMonth(), "YEAR": dateD.getYear()}
			});
			$scope.posts = posts;
			//$scope.dates = datestrings;
		});
		console.log($scope)
});