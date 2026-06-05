import type { CSSProperties } from "react";

const particles = Array.from({ length: 30 }, (_, index) => ({
  id: index,
  x: (index * 37) % 100,
  y: (index * 53) % 100,
  size: 3 + (index % 5),
  delay: (index % 9) * -0.7
}));

export function ParticleField() {
  return (
    <div className="particle-field" aria-hidden="true">
      {particles.map((particle) => (
        <span
          className="particle"
          key={particle.id}
          style={
            {
              "--x": `${particle.x}%`,
              "--y": `${particle.y}%`,
              "--size": `${particle.size}px`,
              "--delay": `${particle.delay}s`
            } as CSSProperties
          }
        />
      ))}
    </div>
  );
}

