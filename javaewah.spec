Name:		javaewah
Version:	1.2.3
Release:	1
Summary:	Word-aligned compressed bitmaps
Group:		Development/Java
License:	ASL 2.0
URL:		https://github.com/lemire/javaewah
Source0:	https://github.com/lemire/javaewah/archive/refs/tags/JavaEWAH-%{version}.tar.gz#/javaewah-%{version}.tar.gz
BuildArch:	noarch
# The jar is plain Java 8. The module descriptor is added by moditect,
# which is not packaged, so that goal is dropped.
%global sysjar_drops --drop org.moditect:moditect-maven-plugin
BuildRequires:	python
BuildRequires:	mvn(org.sonatype.oss:oss-parent:pom::)
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven
BuildOption(install):	--file-name JavaEWAH --link %{name}

%description
JavaEWAH is a 32-bit and 64-bit run-length compressed bitmap. 1.2.3
is the current release on the line that added bitmap shift and fixed
the chunk iterators and BitSet.clear(int).

%prep
%autosetup -n javaewah-JavaEWAH-%{version}
python - <<'PY'
from pathlib import Path
p = Path("pom.xml")
text = p.read_text()
p.write_text(text.replace("<packaging>bundle</packaging>", "<packaging>jar</packaging>", 1))
PY

%files -f .mfiles
%doc CHANGELOG LICENSE LICENSE-2.0.txt README.md
