/**
 * Funcoes para controle da parte
 * cliente web que interage com 
 * a API no webserver.
 */
(function()
{

    /**
     * Requisicao AJAX para buscar
     * lista de municipios.
     */
    function buscaMunicipio(pagina, filtro)
    {
        
        pagina = pagina || 1;
        
        filtro = filtro || "";

        var req_uri = "http://localhost:5000/municipio/" + filtro;

        $.getJSON({
            'url': req_uri,
            'crossDomain': true,
            'data': {'pagina': pagina}})
        .done(function(data)
        {

            if(data.length<1)
            {

                alert("Não foram encontrados mais registros.");

            }
            else
            {
            
            	preencheLista(data);

            	$('#pagina_atual').val(pagina);
            
            }

        }).fail(function()
        {

            alert("Ocorreu uma falha na requisição dos dados!");

        });

    }

    /**
     * Preenche a tabela HTML com os resultados
     * de busca.
     */
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

    /**
     * Quando o formulario for
     * submetido, faz a busca
     * buscando a primeira pagina
     * de resultados e o filtro
     * digitado.
     */
    $('form').submit(function(e)
    {

        e.preventDefault();

        buscaMunicipio(1, $('input[name=filtro]').val());

    });

    /**
     * Quando se digita enter no
     * campo de busca faz a pesquisa.
     */
    $('#pagina_atual').keypress(function(e)
    {

        if(e.which == 13)
        {
            buscaMunicipio($(this).val(), $('input[name=filtro]').val());
        }

    });

    /**
     * Funcao a ser executada quando
     * clicamos para obter a proxima
     * pagina de registros.
     */
    $("#nav_proximo").click(function(e)
    {

        e.preventDefault();

        var pag = $('#pagina_atual').val();

        $('#pagina_atual').val(pag++);

        buscaMunicipio(pag, $('input[name=filtro]').val());

    });

    /**
     * Funcao a ser executada quando
     * clicamos para obter a pagina
     * ANTERIOR de registros.
     */
    $("#nav_anterior").click(function(e)
    {

        e.preventDefault();

        var pag = $('#pagina_atual').val();

        pag = (pag>1) ? pag - 1 : pag;

        $('#pagina_atual').val(pag);

        buscaMunicipio(pag, $('input[name=filtro]').val());

    });

    /**
     * Funcao executada quando se
     * clica na interrogacao.
     */
    $("#dica").click(function(e)
    {

        e.preventDefault();

        alert("Digite um valor numérico para pesquisar pelo código do IBGE (ex.: 3121001) ou uma palavra para buscar pelo nome do municipio (ex.: Diamantina).");

    });

    /*
     * Quando carrega a pagina jah
     * faz a busca da primeira
     * pagina.
     */
    buscaMunicipio(1);

})();

