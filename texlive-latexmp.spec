Name:		texlive-latexmp
Version:	1.2.1
Release:	1
Summary:	Interface for LaTeX-based typesetting in MetaPost
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/latexmp
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexmp.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexmp.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The MetaPost package latexMP implements a user-friendly
interface to access LaTeX-based typesetting capabilities in
MetaPost. The text to be typeset is given as string. This
allows even dynamic text elements, for example counters, to be
used in labels. Compared to other implementations it is much
more flexible, since it can be used as direct replacement for
btex..etex, and much faster, compared for example to the
solution provided by tex.mp.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metapost/latexmp/latexmp.mp
%doc %{_texmfdistdir}/doc/metapost/latexmp/README
%doc %{_texmfdistdir}/doc/metapost/latexmp/latexmp.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}
