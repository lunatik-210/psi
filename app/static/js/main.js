function setCookie(key, value, expires) 
{
    var d = new Date()
    d.setTime(d.getTime()+(expires*24*60*60*1000));
    document.cookie = key + '=' + value + ';expires=' + d.toUTCString()
}

function getCookie(cname)
{
    var name = cname + "="
    var ca = document.cookie.split(';')
    for(var i=0;i<ca.length;i++)
    {
        var cookie = ca[i]
        while(cookie.charAt(0)==' ')
        {
            cookie = cookie.substring(1)
            if(cookie.indexOf(name) == 0)
            {
                return cookie.substring(name.length,cookie.length);
            }
        }
    }
    return "";
}

//WARNING bullshit code ahead
$(document).ready(function()
{
    var locale_cookie_name = "psi_locale";
    var cookie = getCookie(locale_cookie_name);
    var button = $("#changeLanguageButton");

    button.click(function()
    {
        if(cookie=='en')
        {
            setCookie(locale_cookie_name, 'ru', 30);
        } else if(cookie=='ru')
        {
            setCookie(locale_cookie_name, 'en', 30);
        } else {
            //
        }
        location.reload();
    });
});