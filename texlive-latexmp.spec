Name:		texlive-latexmp
Version:	55643
Release:	2
Summary:	Interface for LaTeX-based typesetting in MetaPost
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/latexmp
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexmp.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexmp.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The MetaPost package latexMP implements a user-friendly
interface to access LaTeX-based typesetting capabilities in
MetaPost. The text to be typeset is given as string. This
allows even dynamic text elements, for example counters, to be
used in labels. Compared to other implementations it is much
more flexible, since it can be used as direct replacement for
btex..etex, and much faster, compared for example to the
solution provided by tex.mp.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metapost/latexmp/latexmp.mp
%doc %{_texmfdistdir}/doc/metapost/latexmp/README
%doc %{_texmfdistdir}/doc/metapost/latexmp/latexmp.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}
