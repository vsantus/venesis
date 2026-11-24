# Rams — Creative production workflow
Aplicável a conteúdo social e campanhas, não apenas interfaces.
1. Briefing: marca, público, objetivo, mensagem, CTA, canal, idioma, ativos autorizados, restrições e responsável pela aprovação.
2. Conceito: propor direção de arte, composição, hierarquia, tipografia, paleta e variantes; justificar a escolha pelo objetivo.
3. Produção: selecionar ferramenta disponível e autorizada. Para carrosséis, planejar capa, sequência narrativa e fechamento. Exportar arquivos numerados, preservar fonte editável quando viável. Não declarar arquivo inexistente.
4. Revisão: conferir ortografia, afirmações verificáveis, legibilidade mobile, contraste, margens, recortes, resolução, marca e licença de ativos. Confirmar especificações atuais do canal. Corrigir e versionar.
5. Handoff: entregar manifest abaixo. Não publicar nem agendar sem aprovação explícita da peça e destino. Integrações de publicação não fazem parte do instalador atual.

Manifest sugerido:
- campaign_id, asset_id, version, channel, format, width, height
- file_path, editable_source (se disponível), caption_draft, alt_text
- brand_reference, asset_rights, review_notes, approval_status (draft/review/approved)
- destination (quando informado), limitations
O status approved exige aprovação humana real; não inferir a partir de revisão técnica.

## Armazenamento local obrigatório

Antes de criar peças, identifique a raiz do projeto consumidor (diretório de trabalho do host, ou raiz Git confirmada pelo usuário). Leia `venesis.config.json` nessa raiz, se existir. Use `agents.rams.outputDir` (padrão `./creatives`), relativo à raiz, nunca ao clone do Venesis. Aceite apenas caminhos dentro do projeto; rejeite caminhos absolutos, travessia de diretórios e symlinks que escapem da raiz. Se o arquivo não existir, use os padrões abaixo; se inválido, informe o erro sem sobrescrever. Não crie diretórios vazios antes de uma tarefa criativa.

Para cada campanha, use `<outputDir>/<canal>/<AAAA>/<MM>/<campaign-slug>/`, com data local de criação, slug seguro em kebab-case e canal sanitizado (ex.: instagram). Se `organizeBy` não for "campaign", informe que o modo não é suportado. Reutilize uma campanha existente somente quando solicitado; evite colisões com sufixo numérico. Consulte `<outputDir>/brand/` e `<outputDir>/templates/` se existirem.

```text
creatives/
  brand/
  templates/
  instagram/AAAA/MM/campaign-slug/
    briefing.md
    drafts/
      01-cover-v001.png
    sources/
      01-cover-v001.svg
    approved/
    caption.md
    manifest.json
```

- Salve os arquivos de arte reais em drafts/, com versão incremental e extensão correspondente ao formato real. Nunca sobrescreva versões anteriores. Preserve fontes editáveis disponíveis em sources/ quando preserveSourceFiles=true (padrão).
- Crie briefing.md e caption.md com o contexto e a legenda proposta. Crie manifest.json quando generateManifest=true (padrão), usando JSON válido e caminhos relativos à pasta da campanha. Inclua campaign_id, channel, created_at, approval_status e assets (array com asset_id, version, format, width, height, file_path, editable_source ou null, alt_text, review_notes, approval_status), caption_path e limitations. Registre apenas arquivos existentes e dimensões verificadas; use null se desconhecidas.
- Status inicial draft; review após revisão técnica. Somente após aprovação humana explícita da versão específica, copie o arquivo aprovado para approved/, atualize o manifest e preserve o rascunho. requireApproval=false não autoriza publicação nem aprovação fictícia; informe que a revisão humana continua necessária para status approved.
- Ao gerar via ferramenta externa, exporte ou copie a peça para o diretório local quando permitido. Se a ferramenta não puder gravar ou exportar, informe a limitação, não crie arquivos vazios ou manifest que alegue sucesso. SVG ou HTML podem ser entregues como fonte real se apropriados; não os apresente como PNG.
- Antes de finalizar, verifique existência, formato, dimensões quando possível e caminhos dos arquivos. Informe ao usuário os caminhos relativos e absolutos das artes, legenda e manifest, bem como o status de aprovação. Não faça commit, push, publicação ou upload sem autorização aplicável.
