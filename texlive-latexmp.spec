%global tl_name latexmp
%global tl_revision 55643

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2.1
Release:	%{tl_revision}.1
Summary:	Interface for LaTeX-based typesetting in MetaPost
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/latexmp
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latexmp.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latexmp.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The MetaPost package latexMP implements a user-friendly interface to
access LaTeX-based typesetting capabilities in MetaPost. The text to be
typeset is given as string. This allows even dynamic text elements, for
example counters, to be used in labels. Compared to other
implementations it is much more flexible, since it can be used as direct
replacement for btex.etex, and much faster, compared for example to the
solution provided by tex.mp.

