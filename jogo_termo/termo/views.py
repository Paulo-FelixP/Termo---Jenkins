from django.shortcuts import render

# 🟩 Função genérica para reaproveitar lógica
def jogar_nivel(request, palavra, template):
    if 'tentativas' not in request.session:
        request.session['tentativas'] = []

    tentativas = request.session['tentativas']
    feedback = None

    if request.method == "POST":
        letras = [request.POST.get(f"letra{i}", "").upper() for i in range(1, len(palavra)+1)]
        palpite = "".join(letras)

        if len(palpite) == len(palavra):
            resultado = []
            letras_usadas = {}

            # Marca verdes
            for i, letra in enumerate(palpite):
                if letra == palavra[i]:
                    resultado.append(("green", letra))
                    letras_usadas[letra] = letras_usadas.get(letra, 0) + 1
                else:
                    resultado.append((None, letra))

            # Marca amarelas e cinzas
            for i, (cor, letra) in enumerate(resultado):
                if cor is None:
                    total_na_palavra = palavra.count(letra)
                    usadas_ate_agora = letras_usadas.get(letra, 0)
                    if letra in palavra and usadas_ate_agora < total_na_palavra:
                        resultado[i] = ("yellow", letra)
                        letras_usadas[letra] = usadas_ate_agora + 1
                    else:
                        resultado[i] = ("gray", letra)

            tentativas.append(resultado)
            request.session['tentativas'] = tentativas

            if palpite == palavra:
                feedback = "acertou"
            elif len(tentativas) >= 6:
                feedback = "errou"

    elif request.method == "GET":
        # Limpa as tentativas quando entra de novo
        request.session['tentativas'] = []
        tentativas = []

    return render(request, template, {
        'tentativas': tentativas,
        'feedback': feedback,
    })


# 🟩 Nível 1: Palavra "JENKINS"
def nivel1(request):
    return jogar_nivel(request, "JENKINS", "termo/nivel1.html")


# 🟨 Nível 2: Palavra "HUDSON"
def nivel2(request):
    return jogar_nivel(request, "HUDSON", "termo/nivel2.html")


# 🟦 Nível 3: Palavra "AUTOMAÇÃO"
def nivel3(request):
    return jogar_nivel(request, "AUTOMAÇÃO", "termo/nivel3.html")
