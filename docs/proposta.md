# Proposta de implementacao: APIs oficiais de redes sociais para o Atlas

Data da proposta: 2026-05-11

## Objetivo

Expandir o Atlas para acessar, organizar e acionar dados profissionais e pessoais vindos de redes sociais oficiais, sem depender de scraping. A primeira entrega deve priorizar o LinkedIn, porque e a rede de maior aderencia ao posicionamento profissional do projeto e oferece permissoes self-service para login e publicacao no perfil autenticado.

O anexo analisado foi `apis-sociais-gratuitas.md`, recebido no email "Proposta de utilizacao de APIs oficiais". A direcao estrategica do documento esta correta para LinkedIn e TikTok, mas a parte de X precisa ser atualizada: a documentacao atual da X API descreve um modelo pay-per-use por recurso/requisicao, nao o modelo fixo Free/Basic/Pro usado como base no anexo.

## Validacao em documentacao oficial

### LinkedIn

Fontes oficiais:

- https://learn.microsoft.com/en-us/linkedin/shared/authentication/getting-access
- https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/sign-in-with-linkedin-v2
- https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin
- https://learn.microsoft.com/en-us/linkedin/marketing/community-management/community-management-overview
- https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/posts-api

Pontos validados:

- As permissoes abertas de Consumer incluem `profile`, `email` e `w_member_social`.
- `w_member_social` permite postar, comentar e reagir/curtir em nome do membro autenticado.
- O fluxo recomendado para login e identidade e Sign in with LinkedIn using OpenID Connect, com `openid`, `profile` e `email`.
- Share on LinkedIn pode criar posts de texto, URL e imagem; midia exige registro/upload antes da publicacao.
- APIs de paginas, organizacoes, analytics e gestao de comunidade dependem de acesso aprovado ao Community Management API.
- Leitura ampla de posts, comentarios e likes de membro depende de `r_member_social`, permissao fechada/restrita.

Conclusao: LinkedIn e o melhor ponto de partida para escrita/publicacao profissional e identidade basica, mas nao para leitura ampla de feed ou historico social completo.

### TikTok

Fontes oficiais:

- https://developers.tiktok.com/doc/login-kit-web
- https://developers.tiktok.com/doc/display-api-overview
- https://developers.tiktok.com/doc/display-api-get-started
- https://developers.tiktok.com/doc/content-posting-api-get-started
- https://developers.tiktok.com/doc/research-api-get-started

Pontos validados:

- Login Kit permite obter `access_token` do usuario via OAuth.
- Display API permite ler perfil e videos do usuario autenticado com `user.info.basic` e `video.list`, apos aprovacao dos produtos necessarios.
- Content Posting API permite postagem direta de video/foto, mas o app precisa de aprovacao para `video.publish` e conteudo de clientes nao auditados fica restrito ate auditoria.
- Research API existe para consulta de conteudo publico em escala, mas depende de projeto aprovado e cliente de pesquisa.

Conclusao: TikTok e viavel para identidade, listagem de videos do proprio usuario e publicacao apos aprovacao. Nao deve ser tratado como fonte gratuita de busca ampla por tendencias, hashtags ou historico de terceiros.

### X

Fontes oficiais:

- https://docs.x.com/x-api
- https://docs.x.com/x-api/overview
- https://docs.x.com/x-api/getting-started/getting-access
- https://docs.x.com/x-api/getting-started/pricing
- https://docs.x.com/x-api/posts/create-post
- https://docs.x.com/x-api/media/upload-media

Pontos validados:

- A X API atual e descrita como pay-per-use, com creditos pre-pagos e custo por recurso lido ou requisicao de escrita.
- Reads comuns sao cobrados por recurso; Owned Reads para dados do proprio usuario tem preco reduzido.
- Criacao de conteudo, upload de midia e interacoes tambem aparecem como endpoints disponiveis, com cobranca por requisicao.
- Quote-posting exige Enterprise, segundo a documentacao de criacao de post.

Conclusao: X nao deve ser modelado como integracao gratuita. Para uso pessoal controlado, pode ser implementado com orcamento, cotas internas e telemetria de custo antes de liberar qualquer chamada de leitura.

## Arquitetura proposta

### Principios

- Usar apenas APIs oficiais e OAuth consentido.
- Separar credenciais por provedor e por usuario.
- Nunca expor tokens ao modelo. O agente chama ferramentas, e as ferramentas resolvem autenticacao, escopos, rate limits e auditoria.
- Distinguir claramente capacidades de leitura, escrita e analytics.
- Registrar toda acao externa em log auditavel antes e depois da chamada.
- Exigir confirmacao humana para qualquer acao de escrita publica: publicar, comentar, curtir, repostar, seguir, enviar DM ou apagar conteudo.

### Componentes

1. `ai_agent/social/`
   - Pacote novo para conectores sociais.
   - Um cliente por rede: `linkedin.py`, `tiktok.py`, `x_api.py`.
   - Um modulo comum `oauth.py` para fluxos OAuth, refresh e validacao de state/PKCE quando aplicavel.
   - Um modulo `models.py` com DTOs internos: `SocialProfile`, `SocialPostDraft`, `PublishResult`, `SocialMediaAsset`, `SocialUsage`.

2. `ai_agent/social/token_store.py`
   - Interface de armazenamento de tokens.
   - Para desenvolvimento local: arquivo criptografado ou SQLite local fora do git.
   - Para deploy: Streamlit secrets, banco criptografado ou vault gerenciado.
   - Nunca armazenar tokens em `ai_agent/Context`.

3. `ai_agent/social/audit_log.py`
   - Registro estruturado de consentimento, escopo usado, endpoint, payload resumido, resultado, custo estimado e erro.
   - Nao salvar corpo completo de tokens, segredos ou dados sensiveis.

4. `ai_agent/tools_social.py`
   - Ferramentas LangChain de alto nivel:
     - `get_social_connection_status`
     - `get_linkedin_profile`
     - `draft_linkedin_post`
     - `publish_linkedin_post`
     - `list_tiktok_profile_videos`
     - `publish_tiktok_video`
     - `estimate_x_api_cost`
     - `publish_x_post`
   - Ferramentas de escrita devem recusar execucao sem confirmacao explicita.

5. `pages/social.py`
   - Pagina Streamlit para conectar contas, revisar escopos, ver status de tokens, desconectar provedores e aprovar posts.
   - Essa pagina deve ser o caminho padrao para consentimento e revisao visual antes de qualquer publicacao.

## Proposta por rede social

### 1. LinkedIn

Prioridade: alta.

Capacidades MVP:

- Conectar conta via OIDC com `openid`, `profile`, `email`.
- Obter identidade profissional basica do usuario autenticado.
- Preparar rascunhos de posts a partir do historico profissional existente no Atlas.
- Publicar posts de texto e links com `w_member_social`.
- Publicar imagem/video em fase seguinte, apos implementar fluxo de upload de midia.
- Comentar e reagir somente com confirmacao explicita e somente quando houver um URN de post fornecido pelo usuario.

Escopos:

- `openid`
- `profile`
- `email`
- `w_member_social`

Arquitetura especifica:

- `LinkedInClient`
  - `build_authorization_url(scopes)`
  - `exchange_code_for_token(code)`
  - `refresh_access_token(refresh_token)`
  - `get_userinfo()`
  - `create_text_post(author_urn, text, visibility)`
  - `create_url_post(author_urn, text, url, title=None, description=None)`
  - `register_media_upload(...)`
  - `create_media_post(...)`

Fluxo de publicacao:

1. Usuario pede ao Atlas para criar um post.
2. Atlas gera rascunho, sem chamar LinkedIn.
3. Usuario revisa no Streamlit.
4. Ferramenta valida tamanho, URLs, midias e escopo.
5. Usuario confirma.
6. `LinkedInClient` publica.
7. `audit_log` registra request resumido e `post_urn`.

Limitacoes:

- Nao ha leitura ampla de feed via permissoes abertas.
- Analytics, paginas de empresa e gestao de comunidade exigem Community Management/Marketing API aprovado.
- `r_member_social` e fechado, portanto nao deve ser premissa do MVP.

### 2. TikTok

Prioridade: media.

Capacidades MVP:

- Conectar conta via Login Kit.
- Ler perfil do usuario autenticado.
- Listar videos recentes do proprio usuario com Display API.
- Criar inventario local de videos publicados para enriquecer o contexto do Atlas.
- Preparar publicacao, mas manter Direct Post atras de feature flag ate aprovacao/auditoria do app.

Escopos:

- `user.info.basic`
- `video.list`
- `video.publish` apenas quando o app estiver aprovado para Content Posting API.

Arquitetura especifica:

- `TikTokClient`
  - `build_authorization_url(scopes)`
  - `exchange_code_for_token(code)`
  - `refresh_access_token(refresh_token)`
  - `get_user_info(fields)`
  - `list_videos(fields, max_count, cursor=None)`
  - `query_creator_info()`
  - `init_video_post(...)`
  - `fetch_post_status(publish_id)`

Fluxo recomendado:

1. Implementar Login Kit e Display API primeiro.
2. Guardar metadados dos videos do usuario em cache local com TTL.
3. Expor ferramenta `list_tiktok_profile_videos` para o Atlas responder sobre conteudo proprio.
4. Implementar postagem somente depois de validar aprovacao de produto, limites, auditoria e requisitos de dominio/URL para midia.

Limitacoes:

- Display API nao e mecanismo de busca em escala.
- Publicacao direta depende de aprovacao de `video.publish`.
- Conteudo de cliente nao auditado pode ficar restrito a visibilidade privada ate auditoria.
- Research API deve ser tratado como caminho separado e aprovado, nao como recurso padrao do agente pessoal.

### 3. X

Prioridade: baixa para MVP gratuito; media se houver orcamento controlado.

Capacidades MVP:

- Tela de configuracao para credenciais e orcamento maximo.
- Estimador de custo antes de qualquer acao.
- Publicacao simples de post, se o usuario quiser habilitar pay-per-use.
- Leitura de dados proprios usando Owned Reads somente com budget e cache.
- Upload de midia somente apos validacao do custo e do endpoint no console.

Arquitetura especifica:

- `XClient`
  - `get_usage()`
  - `estimate_cost(operation, expected_resources)`
  - `create_post(text, media_ids=None)`
  - `upload_media(file_path)`
  - `get_own_posts(user_id, limit)`
  - `get_mentions(user_id, limit)`

Guardrails obrigatorios:

- Variavel `X_API_ENABLED=false` por padrao.
- Variavel `X_API_MONTHLY_BUDGET_USD`.
- Cache e deduplicacao local de recursos lidos por dia.
- Bloqueio automatico ao atingir 80% do budget.
- Confirmacao humana em cada escrita.

Limitacoes:

- A proposta original do anexo cita plano gratuito e Basic de US$ 200/mes; isso nao deve ser usado como base atual.
- A documentacao atual fala em creditos e cobranca por recurso/requisicao.
- Quote-posting exige Enterprise.

## Roadmap recomendado

### Fase 1: Fundacao comum

- Criar `ai_agent/social/`.
- Definir modelos internos e `TokenStore`.
- Criar `audit_log`.
- Criar pagina `pages/social.py` para status e consentimento.
- Adicionar variaveis de ambiente:
  - `LINKEDIN_CLIENT_ID`
  - `LINKEDIN_CLIENT_SECRET`
  - `LINKEDIN_REDIRECT_URI`
  - `TIKTOK_CLIENT_KEY`
  - `TIKTOK_CLIENT_SECRET`
  - `TIKTOK_REDIRECT_URI`
  - `X_API_ENABLED`
  - `X_API_MONTHLY_BUDGET_USD`

### Fase 2: LinkedIn MVP

- Implementar OAuth/OIDC.
- Implementar `get_linkedin_profile`.
- Implementar rascunho e publicacao de post de texto/link.
- Integrar ferramentas sociais ao `LOCAL_TOOLS` apenas depois de testes locais.
- Adicionar testes unitarios com mock de HTTP para token exchange e publicacao.

### Fase 3: LinkedIn midia e interacoes

- Implementar upload de imagem/video.
- Implementar comentarios/reacoes com confirmacao obrigatoria.
- Adicionar validacao de URN, visibilidade e preview antes do envio.

### Fase 4: TikTok leitura e inventario

- Implementar Login Kit.
- Implementar Display API para perfil e videos.
- Criar cache local dos videos do proprio usuario.
- Expor ferramenta de consulta ao Atlas.

### Fase 5: TikTok publicacao

- Solicitar/aprovar Content Posting API e `video.publish`.
- Implementar Direct Post atras de feature flag.
- Implementar monitoramento de status por `publish_id`.

### Fase 6: X com budget

- Implementar apenas se houver decisao explicita de custo.
- Comecar por estimativa e `get_usage`.
- Liberar leitura de dados proprios com cache.
- Liberar escrita simples depois de budget e confirmacao.

## Criterios de aceite

- Nenhum token ou segredo versionado no git.
- Toda ferramenta social de escrita exige confirmacao explicita.
- Logs de auditoria registram cada chamada externa sem vazar segredos.
- LinkedIn publica post de texto/link em ambiente de desenvolvimento com token consentido.
- TikTok lista perfil/videos do usuario autenticado quando aprovado.
- X bloqueia chamadas quando `X_API_ENABLED` estiver falso ou budget ausente.
- Documentacao interna lista escopos, endpoints e limites conhecidos por provedor.

## Riscos

- Politicas e precos das APIs mudam com frequencia.
- Revisoes de app podem atrasar TikTok e APIs avancadas de LinkedIn.
- Leitura ampla de dados sociais e historico pessoal nao e garantida por APIs abertas.
- Ferramentas de escrita publica precisam de UX de confirmacao para evitar postagem acidental.
- Cotas, custos e versionamento devem ser tratados como parte da arquitetura, nao como detalhe operacional.

## Decisao recomendada

Comecar pelo LinkedIn com um MVP de identidade, rascunho e publicacao revisada. Esse caminho entrega valor profissional imediato ao Atlas, usa permissoes abertas e evita depender de APIs fechadas de leitura. Em seguida, implementar TikTok apenas para leitura do proprio perfil/videos. X deve ficar atras de feature flag e budget por causa do modelo pay-per-use atual.
