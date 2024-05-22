export default function Home() {
  return (
    <main className="_flex _min-h-screen _flex-col _items-center justify-between _p-24">
      <div className="inner-wrap">
        <section className="hero">
          <div className="flex flex-col gap-y-10">
            <h1 className="mb-0">Approve</h1>
            <p className="mb-0">
              Pastel is a powerful tool for marketing teams to review and
              approve marketing collateral like live websites, PDFs and image
              files.
            </p>
            <button className="self-start">Get Started</button>
          </div>
        </section>
        <section className="about">
          <div className="flex flex-col  gap-y-10">
            <h2 className="mb-0">Trusted by world-class marketing teams</h2>
            <p className="mb-0">
              Pastel is a powerful tool for marketing teams to review and
              approve marketing collateral like live websites, PDFs and image
              files.
            </p>
            <button className="self-start">Get Started</button>
          </div>
        </section>
        <section className="features">
            <div className="max-w-2xl mx-auto text-center">
          <div className="flex flex-col gap-y-10">
              <h2 className="mb-0">
                A simple shareable link gets everyone on the same page
              </h2>
              <p className="mb-0 text-balance">
                Review and comment on all your digital marketing assets. All in
                one place. Share it securely with a link.
              </p>
              <button>Get Started</button>
            </div>
          </div>
        </section>
      </div>
    </main>
  );
}
