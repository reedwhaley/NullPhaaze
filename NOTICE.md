# Source and integration notices

The aggregate RDS-backed backend is GPL-3.0-only. `LICENSE` retains that license;
`src/nullphaze_core/LICENSE` retains the original core's MIT grant. The catalog's
reference-derived IDs, templates and dependency facts keep their attribution in
`src/nullphaze_core/data/provenance.json`. This is not a clean-room claim.

The CDV/Randovania integration retains its existing GPL notices, including
`integrations/cdv/overlay/cdv/LICENSE` and the networking addon's license and
`VENDOR_PROVENANCE.json`. The MP3Update zipline port retains its MIT notice in the
exporter directory. No MP3Update executable or recovered C# implementation is
included. Model inputs and game media are supplied locally by the user.

The vendored RDS project retains its GPL license, generated-reader MIT attribution
and RSOT license. Its 1,876 Python sources are byte-for-byte the corrected pinned
project identified in its `NOTICE.md`. I keep those readers intact and put their
file-specific notation in `SOURCE_MANIFEST.json`; changing generated source to
add prose would obscure the exact prerequisite we validated.

The new comments explain existing behavior. Data and license files keep their
original bytes, with technical notes attached to their manifest entries. Build
and integration scripts identify their changes explicitly in the source manifest.
