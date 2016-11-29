/**
 * Created by allegro_l on 26/11/16.
 */
    console.log("hello world2");
    var OSName="Unknown OS";
    if (navigator.appVersion.indexOf("Win")!=-1) OSName="Windows";
    if (navigator.appVersion.indexOf("Mac")!=-1) OSName="MacOS";
    if (navigator.appVersion.indexOf("X11")!=-1) OSName="UNIX";
    if (navigator.appVersion.indexOf("Linux")!=-1) OSName="Linux";
    console.log(OSName);
    navigator.sayswho= (function(){
      var ua= navigator.userAgent, tem,
      M= ua.match(/(opera|chrome|safari|firefox|msie|trident(?=\/))\/?\s*(\d+)/i) || [];
      if(/trident/i.test(M[1])){
        tem=  /\brv[ :]+(\d+)/g.exec(ua) || [];
        return 'IE '+(tem[1] || '');
      }
      if(M[1]=== 'Chrome'){
        tem= ua.match(/\b(OPR|Edge)\/(\d+)/);
        if(tem!= null) return tem.slice(1).join(' ').replace('OPR', 'Opera');
      }
      M= M[2]? [M[1], M[2]]: [navigator.appName, navigator.appVersion, '-?'];
      if((tem= ua.match(/version\/(\d+)/i))!= null) M.splice(1, 1, tem[1]);
      return M[0];
    })();
    console.log(navigator.sayswho);
    var addr="http://127.0.0.1:8000/";
    var app = angular.module('usr_data', []);
    app.config(['$httpProvider', function($httpProvider) {
      $httpProvider.defaults.headers.common['X-CSRFToken'] = '{{ csrf_token|escapejs }}';
    }]);
    app.controller('usr_control', function($scope, $http) {
    // deprecated part for $http get, for testing use
    //   $scope.func_ck = function() {
    //     $http({
    //         method : "GET",
    //         url : "http://127.0.0.1:8000/users/loc/callloc1"
    //     }).then(function mySucces(response) {
    //         console.log(response.data);
    //     }, function myError(response) {
    //         window.alert("not" + response.data);
    //     });
    //   };
        $scope.func_submit = function() {
          var key1=$scope.md;
          key1.os = OSName;
          key1.browser = navigator.sayswho;

          if(key1.gender=="not to provide"){
              key1.gender="-unknown-";
          }
          switch(key1.language) {
            case "English":
                key1.language='en';
                break;
            case "German":
                key1.language='de';
                break;
            case "Italian":
                key1.language='it';
                break;
            case "Others":
                key1.language='ot';
                break;
              default:
                  console.log(key1.language);
                break;
          }
          $http({
            method : "POST",
            url : addr+"users/",
            data: key1
          }).then(function mySucces(response) {
            window.alert("sucess");
            console.log(response.data);
            // location.reload();
              var redir="/usersloc/"+key1.account;
              window.location='/usersloc/'+key1.account;
          }, function myError(response) {
            window.alert("not" + response.data);
          });
        };
      });
