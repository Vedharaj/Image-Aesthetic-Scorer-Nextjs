import React from "react";
import { cn } from "@/lib/utils";

type CardProps = {
  children: React.ReactNode;
  className?: string;
};

type CardHeaderProps = {
  title: string;
  subtitle?: string;
};

type CardContentProps = {
  children: React.ReactNode;
};

export function Card({ children, className }: CardProps) {
  return (
    <div
      className={cn(
        "bg-white rounded-2xl shadow-lg border border-gray-200 p-6 w-full max-w-md",
        className
      )}
    >
      {children}
    </div>
  );
}

export function CardHeader({ title, subtitle }: CardHeaderProps) {
  return (
    <div className="text-center mb-4">
      <h2 className="text-2xl font-bold text-gray-800">{title}</h2>
      {subtitle && <p className="text-sm text-gray-500 mt-1">{subtitle}</p>}
    </div>
  );
}

export function CardContent({ children }: CardContentProps) {
  return <div className="mt-2">{children}</div>;
}
