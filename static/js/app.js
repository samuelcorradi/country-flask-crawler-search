/**
 * Requisicao AJAX para buscar
 * lista de municipios.
 */
function buscaMunicipio(pag, filtro)
{
    
    pag = pag || 1;
    
    filtro = filtro || "";

    $.ajax({'url': "http://localhost:5000/municipio/" + pag + "/" + filtro, 'crossDomain': true})
    .done(function(data)
    {

        json = jQuery.parseJSON(data);

        console.log(json);

        if(json.length<1)
        {
            alert("Não foram encontrados mais registros.");
        }

        preencheLista(json);

        $('#pagina_atual').val(pag);

    });

}

function preencheLista(data)
{

    var body = $('content table tbody');

    body.empty();
    
    for(var i = 0; i<data.length; i++)
    {
        body.append("<tr><td>" + data[i]['ibge'] + "</td><td>" +
            data[i]['nome'] + "</td><td>" +
            data[i]['url'] + "</td></tr>");
    }

}

$(function()
{

    buscaMunicipio(1);

    $('form').submit(function(e)
    {

        e.preventDefault();

        buscaMunicipio(1, $('input[name=filtro]').val());

    });

    $('#pagina_atual').keypress(function(e)
    {

        if(e.which == 13)
        {

            console.log($(this).val());

            buscaMunicipio($(this).val(), $('input[name=filtro]').val());
        
        }

    });

    $("#nav_proximo").click(function(e)
    {

        e.preventDefault();

        var pag = $('#pagina_atual').val();

        $('#pagina_atual').val(pag++);

        buscaMunicipio(pag, $('input[name=filtro]').val());

    });

    $("#nav_anterior").click(function(e)
    {

        e.preventDefault();

        var pag = $('#pagina_atual').val();

        pag = (pag>1) ? pag - 1 : pag;

        $('#pagina_atual').val(pag);

        buscaMunicipio(pag, $('input[name=filtro]').val());

    });

    $("#dica").click(function(e)
    {

        e.preventDefault();

        alert("Digite um valor numérico para pesquisar pelo código do IBGE (ex.: 3121001) ou uma palavra para buscar pelo nome do municipio (ex.: Diamantina).");

    });

});

