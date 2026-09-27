#!/usr/bin/env bash
# Copia o ECC (Everything Claude Code) para dentro de .claude/ deste repositório,
# para que os comandos /ecc:... funcionem também nas sessões do Claude Code na nuvem.
#
# Uso:  bash .claude/ecc-sync.sh [ref]
#       ref = branch ou tag do ECC (padrão: branch principal)
#
# O que é copiado:
#   commands/*.md  -> .claude/commands/ecc/   (viram /ecc:<nome>, como no plugin)
#   agents/*.md    -> .claude/agents/
#   skills/<nome>/ -> .claude/skills/<nome>/
# Hooks e rules do ECC não são copiados.
#
# Os arquivos do ECC ficam listados em .claude/ecc-manifest.txt; ao rodar de novo,
# só eles são apagados e recopiados (skills e agentes seus não são tocados).
set -euo pipefail

REPO_URL="https://github.com/affaan-m/everything-claude-code"
REF="${1:-}"

# Skills do ECC com o mesmo nome de um comando embutido do Claude Code
# ganham o prefixo "ecc-" para não esconder o comando embutido.
RESERVED_SKILLS="security-review code-review simplify loop init run review"

DST="$(cd "$(dirname "$0")" && pwd)"
MANIFEST="$DST/ecc-manifest.txt"

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

echo "Baixando ECC${REF:+ ($REF)}..."
git clone -q --depth 1 ${REF:+--branch "$REF"} "$REPO_URL" "$TMP/ecc"
SRC="$TMP/ecc"

if [ -f "$MANIFEST" ]; then
  echo "Removendo a cópia anterior..."
  { grep -v '^#' "$MANIFEST" || true; } | while IFS= read -r path; do
    if [ -n "$path" ]; then rm -rf "${DST:?}/$path"; fi
  done
fi

mkdir -p "$DST/commands/ecc" "$DST/agents" "$DST/skills"
entries=()

cp "$SRC"/commands/*.md "$DST/commands/ecc/"
entries+=("commands/ecc")

for f in "$SRC"/agents/*.md; do
  cp "$f" "$DST/agents/"
  entries+=("agents/$(basename "$f")")
done

for d in "$SRC"/skills/*/; do
  name="$(basename "$d")"
  [ -f "$d/SKILL.md" ] || continue
  target="$name"
  if [[ " $RESERVED_SKILLS " == *" $name "* ]]; then
    target="ecc-$name"
  fi
  if [ -e "$DST/skills/$target" ]; then
    echo "Aviso: .claude/skills/$target já existe e não é do ECC; pulando." >&2
    continue
  fi
  cp -R "$d" "$DST/skills/$target"
  if [ "$target" != "$name" ]; then
    sed -i.bak "s/^name: $name\$/name: $target/" "$DST/skills/$target/SKILL.md"
    rm -f "$DST/skills/$target/SKILL.md.bak"
  fi
  entries+=("skills/$target")
done

cp "$SRC/LICENSE" "$DST/ECC-LICENSE"
entries+=("ECC-LICENSE")

{
  echo "# ECC $(cat "$SRC/VERSION") — commit $(git -C "$SRC" rev-parse --short HEAD) ($(git -C "$SRC" log -1 --format=%cs))"
  echo "# Gerado por .claude/ecc-sync.sh. Não edite à mão."
  printf '%s\n' "${entries[@]}"
} > "$MANIFEST"

echo "Pronto: $(ls "$DST/commands/ecc" | wc -l | tr -d ' ') comandos, $(grep -c '^agents/' "$MANIFEST") agentes, $(grep -c '^skills/' "$MANIFEST") skills."
echo "Abra uma nova sessão para os comandos aparecerem."
