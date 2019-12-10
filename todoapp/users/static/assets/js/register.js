/**
 * Alien v1.0.0 - Alien - Trendy Multipurpose Template
 * @link 
 * @copyright 2016-2017 ThemeBucket
 * @license ISC
 */




;(function () {
    'use strict';




    $('.signInButt').on('click', function(e) {
        e.preventDefault();
        var data = {};
        data.username = $('.username_login').val()
        data.password = $('.password_login').val()
        var json = JSON.stringify(data);

        $.ajax({
            type: "POST",
            url: "api/users/login/",
            data: json,
            contentType: "application/json",
            success: function (data) {

                window.location.replace("/profile");
                console.log(data)


            },
            error: function(data) {

                var txt = '';
                var i = 0;
                $.each(data.responseJSON, function(index, value) {
                    txt += index+' : '+value[0]+' \n';
                });
                const Toast = Swal.mixin({
                  toast: true,
                  position: 'top-right',
                  showConfirmButton: false,
                  timer: 5000,
                  timerProgressBar: true,
                  onOpen: (toast) => {
                    toast.addEventListener('mouseenter', Swal.stopTimer)
                    toast.addEventListener('mouseleave', Swal.resumeTimer)
                  }
                })
                Toast.fire({
                  icon: 'error',
                  title: txt
                })

            }
        });


    });

    $('.registerBtnAgain').on('click', function(e) {
        e.preventDefault();
        var timerInterval
        var time_m = 60
        var k
        const { value: formValues } =  Swal.fire({
          timer: 600000,
          timerProgressBar: true,
          title: 'validate number',
          html:
            '<input placeholder="phone number" id="swal-input1" class="swal2-input">' +
            '<input placeholder="code" id="swal-input2" class="swal2-input">',

          focusConfirm: false,

          preConfirm: () => {
            clearInterval(k)
            var data = {};
            data.username = document.getElementById('swal-input1').value
            data.verify_code = document.getElementById('swal-input2').value
            var json = JSON.stringify(data);
            $.ajax({
                type: "POST",
                url: "api/users/verify",
                data: json,
                contentType: "application/json",
                success: function (data) {

                    const Toast = Swal.mixin({
                      toast: true,
                      position: 'top-end',
                      showConfirmButton: false,
                      timer: 3000,
                      timerProgressBar: true,
                      onOpen: (toast) => {
                        toast.addEventListener('mouseenter', Swal.stopTimer)
                        toast.addEventListener('mouseleave', Swal.resumeTimer)
                      }
                    })

                    Toast.fire({
                      icon: 'success',
                      title: data
                    })

                    console.log(data)


                },
                error: function(data) {



                    const Toast = Swal.mixin({
                      toast: true,
                      position: 'top-end',
                      showConfirmButton: false,
                      timer: 3000,
                      timerProgressBar: true,
                      onOpen: (toast) => {
                        toast.addEventListener('mouseenter', Swal.stopTimer)
                        toast.addEventListener('mouseleave', Swal.resumeTimer)
                      }
                    })

                    Toast.fire({
                      icon: 'error',
                      title: data.responseText
                    })


                }
            });











          }
        })








    });


















    $('.registerBtn').on('click', function(e) {
        e.preventDefault();
        var timerInterval
        var time_m = 6
        var k
        var frm = $('#register_form');
        var data = {};
        data.username = $('.username_f').val()
        data.password = $('.password_f').val()
        data.type = $('.type_f').val()
        console.log(data.type)
        data.confirm_password = $('.password_f2').val()
        var json = JSON.stringify(data);
        $.ajax({
            type: "POST",
            url: "api/users/",
            data: json,
            contentType: "application/json",
            success: function (data) {

                Swal.fire({
                  title: 'auth code pls ',
                  input: 'text',
                  html:'<div id="timer_box"> <span id="time_txt"> time : </span><span id="time_span"> </span> <span style="display:none" id="resend_code">resend code </span>      </div>',
                  inputAttributes: {
                    autocapitalize: 'off'
                  },
                  showCancelButton: false,
                  confirmButtonText: 'Send',
                  showLoaderOnConfirm: true,

                  onBeforeOpen: () => {
                     k = setInterval(function(){
                        time_m--

                        if(time_m > 0 ){
                            $('#time_span').html(time_m)
                        }else{
                            var myEl = document.getElementById('resend_code');

                            myEl.addEventListener('click', function() {
                                var data = {};
                                data.username = $('.username_f').val()
                                data.resend_code = 'resend_code'
                                var json = JSON.stringify(data);
                                $.ajax({
                                    type: "POST",
                                    url: "api/users/resend_code",
                                    data: json,
                                    contentType: "application/json",
                                    success: function (data) {

                                        $('#resend_code').html(data);


                                    },
                                    error: function(data) {


                                         $('#resend_code').html(data.responseText);


                                    }
                                });






                            }, false);

                            $('#time_span').fadeOut();
                            $('#time_txt').fadeOut();
                            $('#resend_code').fadeIn();
                            clearInterval(k)
                        }

                    }, 1000);


                  },



                  preConfirm: (login) => {
                    var data = {};
                    data.username = $('.username_f').val()
                    data.verify_code = login
                    var json = JSON.stringify(data);
                    $.ajax({
                        type: "POST",
                        url: "api/users/verify",
                        data: json,
                        contentType: "application/json",
                        success: function (data) {

                            const Toast = Swal.mixin({
                              toast: true,
                              position: 'top-end',
                              showConfirmButton: false,
                              timer: 3000,
                              timerProgressBar: true,
                              onOpen: (toast) => {
                                toast.addEventListener('mouseenter', Swal.stopTimer)
                                toast.addEventListener('mouseleave', Swal.resumeTimer)
                              }
                            })

                            Toast.fire({
                              icon: 'success',
                              title: data
                            })

                            console.log(data)


                        },
                        error: function(data) {



                            const Toast = Swal.mixin({
                              toast: true,
                              position: 'top-end',
                              showConfirmButton: false,
                              timer: 3000,
                              timerProgressBar: true,
                              onOpen: (toast) => {
                                toast.addEventListener('mouseenter', Swal.stopTimer)
                                toast.addEventListener('mouseleave', Swal.resumeTimer)
                              }
                            })

                            Toast.fire({
                              icon: 'error',
                              title: data.responseText
                            })


                        }
                    });



                  },
                })


            },
            error: function(data) {
                var txt = '';
                var i = 0;
                $.each(data.responseJSON, function(index, value) {
                    txt += index+' : '+value[0]+' \n';
                });
                const Toast = Swal.mixin({
                  toast: true,
                  position: 'top-right',
                  showConfirmButton: false,
                  timer: 5000,
                  timerProgressBar: true,
                  onOpen: (toast) => {
                    toast.addEventListener('mouseenter', Swal.stopTimer)
                    toast.addEventListener('mouseleave', Swal.resumeTimer)
                  }
                })
                Toast.fire({
                  icon: 'error',
                  title: txt
                })
            }
        });
    });



    $('#resend_code').on('click', function(e) {
        alert('asd')
    });



})(jQuery);


