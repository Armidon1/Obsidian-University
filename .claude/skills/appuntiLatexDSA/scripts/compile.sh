#!/usr/bin/env bash
# Compila main.tex di una cartella di appunti con LuaLaTeX.
#
# uso: compile.sh <cartella-appunti> [--pull]
#
# Usa latexmk e lualatex locali se ci sono, altrimenti podman o docker con TeX Live.
# Se l'immagine manca si ferma, perché pesa circa 6 GB: --pull autorizza a scaricarla.
# L'output completo finisce in <cartella>/build.log. L'exit code è quello di latexmk.
set -u

dir=""
pull=0
for arg in "$@"; do
  case "$arg" in
    --pull) pull=1 ;;
    *) dir="$arg" ;;
  esac
done
if [ -z "$dir" ] || [ ! -f "$dir/main.tex" ]; then
  echo "uso: compile.sh <cartella-con-main.tex> [--pull]" >&2
  exit 2
fi
dir=$(cd "$dir" && pwd)
image="docker.io/texlive/texlive:latest"
latexmk_cmd=(latexmk -lualatex -interaction=nonstopmode -halt-on-error main.tex)

if command -v latexmk >/dev/null 2>&1 && command -v lualatex >/dev/null 2>&1; then
  (cd "$dir" && "${latexmk_cmd[@]}") >"$dir/build.log" 2>&1
  code=$?
else
  if command -v podman >/dev/null 2>&1; then
    engine=podman
    mount="$dir:/work:Z"
    user_args=()
  elif command -v docker >/dev/null 2>&1; then
    engine=docker
    mount="$dir:/work"
    user_args=(--user "$(id -u):$(id -g)")
  else
    echo "Serve latexmk con lualatex, oppure podman o docker." >&2
    exit 3
  fi
  if ! "$engine" image exists "$image" 2>/dev/null && ! "$engine" image inspect "$image" >/dev/null 2>&1; then
    if [ "$pull" -eq 0 ]; then
      echo "Immagine $image assente (circa 6 GB): rilancia con --pull per scaricarla." >&2
      exit 4
    fi
    "$engine" pull "$image" || exit 4
  fi
  "$engine" run --rm "${user_args[@]}" -v "$mount" -w /work "$image" "${latexmk_cmd[@]}" >"$dir/build.log" 2>&1
  code=$?
fi

if [ "$code" -ne 0 ]; then
  echo "Compilazione fallita (exit $code)."
  grep -n -A3 '^!' "$dir/main.log" 2>/dev/null | head -30
  echo "Log completo: $dir/build.log"
else
  echo "OK: $dir/main.pdf ($(pdfinfo "$dir/main.pdf" 2>/dev/null | awk '/^Pages/{print $2}') pagine, $(du -h "$dir/main.pdf" | cut -f1))"
fi
exit "$code"
