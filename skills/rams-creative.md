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
