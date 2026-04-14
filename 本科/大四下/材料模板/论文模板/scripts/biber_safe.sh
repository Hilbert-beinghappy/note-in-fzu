#!/bin/sh
set -eu

# MacTeX biber 2.20 can fail inside the packed PAR runtime on this machine:
# - missing Unicode::UCD unicore/version from the extracted runtime
# - transient lipo extraction failures when the PAR temp dir is unstable/shared
# Prepend the system Perl core library and force a fresh per-invocation PAR dir.

perl_core="/System/Library/Perl/5.34"
if [ -n "${PERL5LIB:-}" ]; then
  export PERL5LIB="${perl_core}:${PERL5LIB}"
else
  export PERL5LIB="${perl_core}"
fi

par_tmpdir="$(mktemp -d "${TMPDIR:-/tmp}/biber-par.XXXXXX")"
cleanup() {
  rm -rf "${par_tmpdir}"
}
trap cleanup EXIT HUP INT TERM
export PAR_GLOBAL_TMPDIR="${par_tmpdir}"

biber "$@"
