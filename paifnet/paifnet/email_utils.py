# # paifnet/views.py
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# def send_email(nome, email, telefone, problema):
#     remetente = "josehenriquese125@gmail.com"
#     senha = "sua_senha"  # Evite expor senhas diretamente no código, use variáveis de ambiente
#     destinatario = "josehenriquese125@gmail.com"

#     msg = MIMEMultipart()
#     msg['From'] = remetente
#     msg['To'] = destinatario
#     msg['Subject'] = "Novo Relato de Suporte"

#     corpo = f"""
#     Novo relato de suporte recebido:

#     Nome: {nome}
#     Email: {email}
#     Telefone: {telefone}
#     Problema: {problema}
#     """
    
#     msg.attach(MIMEText(corpo, 'plain'))

#     try:
#         with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
#             server.login(remetente, senha)
#             server.sendmail(remetente, destinatario, msg.as_string())
#             print("E-mail enviado com sucesso!")
#     except Exception as e:
#         print(f"Erro ao enviar e-mail: {e}")

# # Função para processar o formulário de suporte
# @verificar_cookie
# def form_suporte(request):
#     if request.method == 'POST':
#         nome = request.POST.get('nome')
#         email = request.POST.get('email')
#         telefone = request.POST.get('telefone')
#         problema = request.POST.get('problema')

#         try:
#             # Salvar no Firestore
#             doc_ref = db.collection("suporte").add({
#                 'nome': nome,
#                 'email': email,
#                 'telefone': telefone,
#                 'problema': problema,
#             })

#             # Obter ID e atualizar com o campo 'id'
#             document_id = doc_ref.id
#             doc_ref.update({
#                 'id': document_id
#             })

#             # Enviar o e-mail
#             send_email(nome, email, telefone, problema)

#             # Após salvar, renderiza a página de sucesso
#             return render(request, 'form_suporte/sucesso.html', {'nome': nome})
#         except Exception as e:
#             print(f"Erro: {e}")
#             return render(request, 'form_suporte/form_suporte.html', {'erro': "Erro ao salvar ou enviar e-mail."})

#     return render(request, 'form_suporte/form_suporte.html')
