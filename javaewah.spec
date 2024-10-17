%{?_javapackages_macros:%_javapackages_macros}
%global commit 19ea785bb7d5d37eaaf39a52bda3a3f32385577b
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           javaewah
Version:        0.7.9
Release:        2.0%{?dist}
Summary:        A word-aligned compressed variant of the Java bitset class


License:        ASL 2.0
URL:            https://code.google.com/p/javaewah/
Source0:        https://github.com/lemire/%{name}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildArch:      noarch

BuildRequires: maven-local
BuildRequires: maven-surefire-provider-junit4


%description
JavaEWAH is a word-aligned compressed variant of the Java bitset class.
It uses a 64-bit run-length encoding (RLE) compression scheme.

The goal of word-aligned compression is not to achieve the best
compression, but rather to improve query processing time. Hence, we try
to save CPU cycles, maybe at the expense of storage. However, the EWAH
scheme we implemented is always more efficient storage-wise than an
uncompressed bitmap (implemented in Java as the BitSet class). Unlike
some alternatives, javaewah does not rely on a patented scheme.

%package javadoc

Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.


%prep
%setup -qn %{name}-%{commit}

%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin

%build
# Tests pass locally, but not in koji for some reason
%mvn_build --skip-tests

%install
%mvn_install

%files -f .mfiles
%doc CHANGELOG README.md LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Sat Nov 16 2013 Gerard Ryan <galileo@fedoraproject.org> - 0.7.9-2
- Skip tests since they prevent building in koji

* Sat Nov 16 2013 Gerard Ryan <galileo@fedoraproject.org> - 0.7.9-1
- Update to 0.7.9 to fix license ambiguity

* Thu Oct 10 2013 Gerard Ryan <galileo@fedoraproject.org> - 0.7.8-1
- Update to latest upstream version

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 09 2013 Gerard Ryan <galileo@fedoraproject.org> - 0.6.12-1
- Initial package.
