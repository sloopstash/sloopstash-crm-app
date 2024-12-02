/*!
 * Classic theme main functionalities.
 */

$(document).ready(function() {

  $('.dropdown-trigger').dropdown({constrainWidth:false,hover:true});
  $('.sidenav').sidenav();
  $('.rightsidenav').sidenav({'edge':'right','width':500});
  $('.tooltipped').tooltip({'margin':0});
  $('.tabs').tabs();
  $('select').formSelect();
  $('.modal').modal({dismissible:false});
  $('.collapsible').collapsible();
  $('.datepicker').datepicker({
    format:'mmm dd yyyy',
    setDefaultDate:true
  });
});
